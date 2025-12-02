
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
key = 'Fm'

# Bar duration in seconds (at 160 BPM, 4/4 time)
bar_duration = 6.0  # 6 seconds for 4 bars
note_duration = 0.375  # 1 beat = 0.375s at 160 BPM
rest = 0.0  # No rest unless specified

# Create instruments
sax_instrument = Instrument(program=Program.SAXOPHONE_ALTO, is_drum=False)
bass_instrument = Instrument(program=Program.BASS_FRETLESS, is_drum=False)
piano_instrument = Instrument(program=Program.PIANO_GRAND, is_drum=False)
drum_instrument = Instrument(program=Program.DRUMS, is_drum=True)

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drum_instrument]

# --- DRUMS: Little Ray on 1 and 3 (kick), 2 and 4 (snare), hihat on every eighth (bar 1 only)---
# Bar 1: Kick, Snare, Hihat on all eighths
# Bar 2-4: Kick on 1 and 3, Snare on 2 and 4

def add_drum_notes(instrument, time, kick, snare, hihat):
    if kick:
        instrument.notes.append(Note(36, 100, time, time + note_duration))
    if snare:
        instrument.notes.append(Note(38, 100, time, time + note_duration))
    if hihat:
        instrument.notes.append(Note(42, 100, time, time + note_duration))

# Bar 1
add_drum_notes(drum_instrument, 0.0, True, False, True)
add_drum_notes(drum_instrument, 0.375, False, False, True)
add_drum_notes(drum_instrument, 0.75, False, False, True)
add_drum_notes(drum_instrument, 1.125, False, False, True)
add_drum_notes(drum_instrument, 1.5, True, False, True)
add_drum_notes(drum_instrument, 1.875, False, False, True)
add_drum_notes(drum_instrument, 2.25, False, False, True)
add_drum_notes(drum_instrument, 2.625, False, False, True)
add_drum_notes(drum_instrument, 3.0, False, True, True)  # Snare on the "and" of 4

# Bar 2-4: Kick on 1 and 3, Snare on 2 and 4
for bar in range(2, 5):
    start_time = bar * note_duration * 3  # 3 beats per bar already passed in bar 1
    add_drum_notes(drum_instrument, start_time, True, False, False)
    add_drum_notes(drum_instrument, start_time + note_duration, False, True, False)
    add_drum_notes(drum_instrument, start_time + note_duration * 2, True, False, False)
    add_drum_notes(drum_instrument, start_time + note_duration * 3, False, True, False)

# --- BASS: Marcus on walking line, chromatic approaches, no repeated notes ---
# Fm7 chord: F, Ab, Bb, Db
# Walking bass line: F -> Gb -> Ab -> A -> Bb -> B -> C -> Db (chromatic approach)
# Bar 1: Rest (Marcus doesn't play first bar)
# Bar 2-4: Walking line

def add_bass_notes(instrument, time, note, velocity=70):
    instrument.notes.append(Note(note, velocity, time, time + note_duration))

# Bar 2
add_bass_notes(bass_instrument, 3.0, 71)  # F
add_bass_notes(bass_instrument, 3.375, 69)  # Gb
add_bass_notes(bass_instrument, 3.75, 70)  # Ab
add_bass_notes(bass_instrument, 4.125, 72)  # A

# Bar 3
add_bass_notes(bass_instrument, 4.5, 71)  # Bb
add_bass_notes(bass_instrument, 4.875, 72)  # B
add_bass_notes(bass_instrument, 5.25, 74)  # C
add_bass_notes(bass_instrument, 5.625, 70)  # Db

# Bar 4
add_bass_notes(bass_instrument, 6.0, 71)  # F
add_bass_notes(bass_instrument, 6.375, 69)  # Gb
add_bass_notes(bass_instrument, 6.75, 70)  # Ab
add_bass_notes(bass_instrument, 7.125, 72)  # A

# --- PIANO: Diane on 7th chords, comp on 2 and 4 ---
# Fm7 chord: F, Ab, Bb, Db
# Bar 2: Fm7, Bar 3: Fm7, Bar 4: Fm7 (with slight variation)

def add_piano_notes(instrument, time, notes, velocity=80):
    for note in notes:
        instrument.notes.append(Note(note, velocity, time, time + note_duration))

# Bar 2
add_piano_notes(piano_instrument, 3.0, [71, 70, 69, 67])  # F, Ab, Bb, Db

# Bar 3
add_piano_notes(piano_instrument, 4.5, [71, 70, 69, 67])  # F, Ab, Bb, Db

# Bar 4
add_piano_notes(piano_instrument, 6.0, [71, 70, 69, 67])  # F, Ab, Bb, Db

# --- SAX: You on tenor, short motif, leave it hanging, come back and finish it ---
# Motif: F -> Bb -> Ab (playing it over two bars, then resolving in bar 4)

def add_sax_notes(instrument, time, notes, velocity=90):
    for note in notes:
        instrument.notes.append(Note(note, velocity, time, time + note_duration))

# Bar 2: Start the motif
add_sax_notes(sax_instrument, 3.0, [71])  # F

# Bar 3: Continue the motif
add_sax_notes(sax_instrument, 4.5, [69])  # Bb

# Bar 4: Resolve the motif
add_sax_notes(sax_instrument, 6.0, [70])  # Ab
add_sax_notes(sax_instrument, 6.375, [71])  # F (resolve)

# Save the MIDI file
pm.write("f_minor_intro.mid")
print("MIDI file written to 'f_minor_intro.mid'")
