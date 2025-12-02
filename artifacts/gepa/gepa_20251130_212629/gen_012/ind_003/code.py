
import pretty_midi
import numpy as np

# Set up the MIDI file and tempo
pm = pretty_midi.PrettyMidi(initial_tempo=160)
instrument_list = []

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
instrument_list.append(bass)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
instrument_list.append(piano)

drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)
instrument_list.append(drums)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
instrument_list.append(sax)

pm.instruments = instrument_list

# Time parameters
beat = 0.375  # 160 BPM = 60/160 = 0.375 seconds per beat
bar = 4 * beat  # 1.5 seconds per bar
note_duration = 0.25  # quarter note
rest = 0.5  # half rest in bar 1

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3 (bar 0)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))

# Bar 2: Marcus on bass (walking line, chromatic approaches)
# F major scale: F, G, A, Bb, B, C, D, E
# Chromatic descent from B to A in bar 2, then walking bass line

bass_notes = [
    (0.0, 70),  # B (chromatic descent)
    (0.375, 69),  # A
    (0.75, 71),  # B
    (1.125, 72),  # C
    (1.5, 71),  # B
]

# Add the notes
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + note_duration))

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Comp on beat 2 and 4

# Bar 2: Beat 2 (0.75)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=0.75, end=1.0))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=0.75, end=1.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=0.75, end=1.0))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=0.75, end=1.0))  # Eb

# Bar 2: Beat 4 (1.5)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.75))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=1.5, end=1.75))  # Eb

# Bar 3: Marcus continues with walking line
# F major scale walking line

bass_notes = [
    (1.5, 71),  # B
    (1.875, 72),  # C
    (2.25, 74),  # D
    (2.625, 76),  # E
    (3.0, 71),  # B
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + note_duration))

# Diane: F7 again (beat 2 and 4)
# Bar 3: Beat 2 (2.25)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.5))

# Bar 3: Beat 4 (3.0)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.25))

# Bar 4: Dante on sax — the melody

# Motif: F - Bb - C - A (F major, with tension)
# Start at 3.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))  # A

# Rest for half a beat at the end (tension moment)
# The final A is held for half a beat, allowing the silence to speak

# Save the MIDI
pm.write('dante_intro.mid')
