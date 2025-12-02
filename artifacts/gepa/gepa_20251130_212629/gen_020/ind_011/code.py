
import pretty_midi

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to F major
midi.key_signature_changes = [pretty_midi.KeySignature(0, 0)]  # F major

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)
midi.instruments.append(sax)

# Time constants
bar_length = 1.5  # 6 seconds for 4 bars at 160 BPM
beat_length = bar_length / 4  # 0.375 seconds per beat
note_duration = 0.125  # 1/8 note in seconds

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums():
    # Kick
    kick_notes = [pretty_midi.Note(velocity=90, pitch=36, start=0, end=note_duration),
                  pretty_midi.Note(velocity=90, pitch=36, start=2*beat_length, end=2*beat_length + note_duration)]
    drums.notes.extend(kick_notes)

    # Snare
    snare_notes = [pretty_midi.Note(velocity=90, pitch=38, start=1*beat_length, end=1*beat_length + note_duration),
                   pretty_midi.Note(velocity=90, pitch=38, start=3*beat_length, end=3*beat_length + note_duration)]
    drums.notes.extend(snare_notes)

    # Hi-hat (every 8th note)
    for i in range(4):
        hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=i*note_duration, end=i*note_duration + note_duration)]
        drums.notes.extend(hihat_notes)

# Bar 1: Drums only
add_drums()

# Bar 2: Bass enters with walking line (chromatic approaches)
def add_bass():
    # Walking line in F major with chromatic tension
    # F - G - G# - A - A# - Bb - B - C (chromatic under the chord)
    # F7: F A C Eb, but we play chromatic steps in between

    # Bar 2: F - Gb - G - Ab (chromatic line)
    notes = [
        pretty_midi.Note(velocity=80, pitch=65, start=bar_length, end=bar_length + note_duration),  # F
        pretty_midi.Note(velocity=80, pitch=64, start=bar_length + note_duration, end=bar_length + 2*note_duration),  # Gb
        pretty_midi.Note(velocity=80, pitch=66, start=bar_length + 2*note_duration, end=bar_length + 3*note_duration),  # G
        pretty_midi.Note(velocity=80, pitch=67, start=bar_length + 3*note_duration, end=bar_length + 4*note_duration),  # Ab
    ]
    bass.notes.extend(notes)

# Bar 2: Bass
add_bass()

# Bar 2: Piano (comping on 2 and 4 with 7th chords)
def add_piano_bar2():
    # F7 on 2 and 4 (F A C Eb)
    # Start on 2nd beat, end on 3rd
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length + beat_length, end=bar_length + 2*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length + beat_length, end=bar_length + 2*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length + beat_length, end=bar_length + 2*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length + beat_length, end=bar_length + 2*beat_length)  # Eb
    piano.notes.append(note)

    # Repeat on 4th beat
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length + 3*beat_length, end=bar_length + 4*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length + 3*beat_length, end=bar_length + 4*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length + 3*beat_length, end=bar_length + 4*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length + 3*beat_length, end=bar_length + 4*beat_length)  # Eb
    piano.notes.append(note)

# Bar 2: Piano
add_piano_bar2()

# Bar 3: Saxophone enters with motif – short, hanging, incomplete
def add_sax():
    # Motif: F - Ab - Bb (F, Ab, Bb) starts on beat 1
    # End on beat 2, leaving it unresolved
    note1 = pretty_midi.Note(velocity=100, pitch=65, start=bar_length*2, end=bar_length*2 + note_duration)  # F
    sax.notes.append(note1)
    note2 = pretty_midi.Note(velocity=100, pitch=67, start=bar_length*2 + note_duration, end=bar_length*2 + 2*note_duration)  # Ab
    sax.notes.append(note2)
    note3 = pretty_midi.Note(velocity=100, pitch=68, start=bar_length*2 + 2*note_duration, end=bar_length*2 + 3*note_duration)  # Bb
    sax.notes.append(note3)

# Bar 3: Saxophone
add_sax()

# Bar 3: Piano continues comping
def add_piano_bar3():
    # F7 on 2 and 4 again for continuity
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length*2 + beat_length, end=bar_length*2 + 2*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length*2 + beat_length, end=bar_length*2 + 2*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length*2 + beat_length, end=bar_length*2 + 2*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length*2 + beat_length, end=bar_length*2 + 2*beat_length)  # Eb
    piano.notes.append(note)

    # 4th beat
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length*2 + 3*beat_length, end=bar_length*2 + 4*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length*2 + 3*beat_length, end=bar_length*2 + 4*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length*2 + 3*beat_length, end=bar_length*2 + 4*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length*2 + 3*beat_length, end=bar_length*2 + 4*beat_length)  # Eb
    piano.notes.append(note)

# Bar 3: Piano continues
add_piano_bar3()

# Bar 3: Bass continues
def add_bass_bar3():
    # Continue walking line
    # Ab - Bb - B - C (chromatic under the chord)
    notes = [
        pretty_midi.Note(velocity=80, pitch=67, start=bar_length*2, end=bar_length*2 + note_duration),  # Ab
        pretty_midi.Note(velocity=80, pitch=68, start=bar_length*2 + note_duration, end=bar_length*2 + 2*note_duration),  # Bb
        pretty_midi.Note(velocity=80, pitch=69, start=bar_length*2 + 2*note_duration, end=bar_length*2 + 3*note_duration),  # B
        pretty_midi.Note(velocity=80, pitch=72, start=bar_length*2 + 3*note_duration, end=bar_length*2 + 4*note_duration),  # C
    ]
    bass.notes.extend(notes)

# Bar 3: Bass
add_bass_bar3()

# Bar 4: Everyone in again, but saxophone finishes motif
def add_sax_bar4():
    # Finish motif: F - Ab - Bb (but end on Bb and hold it just a little)
    note3 = pretty_midi.Note(velocity=100, pitch=68, start=bar_length*2 + 3*note_duration, end=bar_length*2 + 3.25*note_duration)  # Bb
    sax.notes.append(note3)

# Bar 4: Saxophone finishes
add_sax_bar4()

# Bar 4: Piano continues comping
def add_piano_bar4():
    # F7 on 2 and 4 again
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length*3 + beat_length, end=bar_length*3 + 2*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length*3 + beat_length, end=bar_length*3 + 2*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length*3 + beat_length, end=bar_length*3 + 2*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length*3 + beat_length, end=bar_length*3 + 2*beat_length)  # Eb
    piano.notes.append(note)

    # 4th beat
    note = pretty_midi.Note(velocity=95, pitch=65, start=bar_length*3 + 3*beat_length, end=bar_length*3 + 4*beat_length)  # F
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=68, start=bar_length*3 + 3*beat_length, end=bar_length*3 + 4*beat_length)  # A
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=72, start=bar_length*3 + 3*beat_length, end=bar_length*3 + 4*beat_length)  # C
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=95, pitch=69, start=bar_length*3 + 3*beat_length, end=bar_length*3 + 4*beat_length)  # Eb
    piano.notes.append(note)

# Bar 4: Piano
add_piano_bar4()

# Bar 4: Bass continues walking line
def add_bass_bar4():
    # B - C - C# - D (chromatic line)
    notes = [
        pretty_midi.Note(velocity=80, pitch=69, start=bar_length*3, end=bar_length*3 + note_duration),  # B
        pretty_midi.Note(velocity=80, pitch=72, start=bar_length*3 + note_duration, end=bar_length*3 + 2*note_duration),  # C
        pretty_midi.Note(velocity=80, pitch=73, start=bar_length*3 + 2*note_duration, end=bar_length*3 + 3*note_duration),  # C#
        pretty_midi.Note(velocity=80, pitch=74, start=bar_length*3 + 3*note_duration, end=bar_length*3 + 4*note_duration),  # D
    ]
    bass.notes.extend(notes)

# Bar 4: Bass
add_bass_bar4()

# Bar 4: Drums continue
def add_drums_bar4():
    # Kick on 1 and 3, snare on 2 and 4, hihat every 8th
    # Kick
    kick_notes = [pretty_midi.Note(velocity=90, pitch=36, start=bar_length*3, end=bar_length*3 + note_duration),
                  pretty_midi.Note(velocity=90, pitch=36, start=bar_length*3 + 2*beat_length, end=bar_length*3 + 2*beat_length + note_duration)]
    drums.notes.extend(kick_notes)

    # Snare
    snare_notes = [pretty_midi.Note(velocity=90, pitch=38, start=bar_length*3 + beat_length, end=bar_length*3 + beat_length + note_duration),
                   pretty_midi.Note(velocity=90, pitch=38, start=bar_length*3 + 3*beat_length, end=bar_length*3 + 3*beat_length + note_duration)]
    drums.notes.extend(snare_notes)

    # Hi-hat
    for i in range(4):
        hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_length*3 + i*note_duration, end=bar_length*3 + i*note_duration + note_duration)]
        drums.notes.extend(hihat_notes)

# Bar 4: Drums
add_drums_bar4()

# Write the MIDI file
midi.write("jazz_intro.mid")

print("MIDI file created: jazz_intro.mid")
