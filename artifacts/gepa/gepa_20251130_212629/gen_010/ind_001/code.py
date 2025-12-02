
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to D major
pm.key_signature = pretty_midi.KeySignature(key = pretty_midi.KeySignature.D_MAJOR)

# Define the time signature (4/4)
pm.time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Define the note durations in seconds
beat = 0.375  # 160 BPM, 4/4 time
bar = 4 * beat  # 1.5 seconds per bar

# Define instruments
# Drums (channel 9)
drum_program = pretty_midi.Instrument(program=9)
pm.instruments.append(drum_program)

# Bass (channel 3)
bass_program = pretty_midi.Instrument(program=33)
pm.instruments.append(bass_program)

# Piano (channel 0)
piano_program = pretty_midi.Instrument(program=0)
pm.instruments.append(piano_program)

# Tenor Sax (channel 6)
sax_program = pretty_midi.Instrument(program=64)
pm.instruments.append(sax_program)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 to 1.5 seconds

# Kick on beat 1
drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
# Kick on beat 3
drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5))
# Snare on beat 2
drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125))
# Snare on beat 4
drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875))
# Hihat on every eighth
for i in range(0, 6):
    drum_program.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=i*0.375, end=(i+1)*0.375))

# Bar 2: Bring in bass, piano, and sax
# Time: 1.5 to 3.0 seconds

# Marcus (bass) - walking line with chromatic approaches
# D - C# - B - C - D - E - F# - G - A - B - C - D - C# - B - etc.
bass_notes = [
    (1.5, 62),  # D
    (1.75, 61),  # C#
    (2.0, 60),  # B
    (2.25, 62),  # C
    (2.5, 64),  # D
    (2.75, 65),  # E
    (3.0, 67),  # F#
]
for t, pitch in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25))

# Diane (piano) - 7th chords, comp on 2 and 4
# Time: 1.5 - 3.0
# Chord: D7 on beat 1
piano_notes = [
    # D7 on beat 1 (1.5s)
    (1.5, 62), (1.5, 69), (1.5, 71), (1.5, 67),
    # Rest on beat 2
    # D7 on beat 3 (2.25s)
    (2.25, 62), (2.25, 69), (2.25, 71), (2.25, 67),
    # Rest on beat 4
]
for t, pitch in piano_notes:
    piano_program.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25))

# Dante (sax) - melody starts (first statement)
# Motif: D - F# - C - B (with space)
# Time: 1.5s - 2.25s
sax_notes = [
    (1.5, 62),  # D
    (1.875, 67),  # F#
    (2.25, 60),  # C
    (2.625, 61),  # B
]
for t, pitch in sax_notes:
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25))

# Bar 3: Continue full ensemble
# Time: 3.0 to 4.5 seconds

# Marcus (bass) continues walking line
bass_notes = [
    (3.0, 69),  # G
    (3.25, 71),  # A
    (3.5, 69),  # G
    (3.75, 67),  # F#
    (4.0, 65),  # E
    (4.25, 64),  # D
    (4.5, 62),  # C
]
for t, pitch in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25))

# Diane (piano) continues comping on 2 and 4
piano_notes = [
    # G7 on beat 1 (3.0s)
    (3.0, 67), (3.0, 74), (3.0, 76), (3.0, 72),
    # Rest on beat 2
    # G7 on beat 3 (3.75s)
    (3.75, 67), (3.75, 74), (3.75, 76), (3.75, 72),
    # Rest on beat 4
]
for t, pitch in piano_notes:
    piano_program.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25))

# Dante (sax) - second statement of motif, variation
# Motif: B - D - F# - G (with space)
sax_notes = [
    (3.0, 61),  # B
    (3.375, 62),  # D
    (3.75, 67),  # F#
    (4.125, 69),  # G
]
for t, pitch in sax_notes:
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25))

# Bar 4: Final bar, build tension with space and resolution
# Time: 4.5 to 6.0 seconds

# Marcus (bass) continues with E - D - C - B
bass_notes = [
    (4.5, 64),  # E
    (4.75, 62),  # D
    (5.0, 60),  # C
    (5.25, 59),  # B
]
for t, pitch in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25))

# Diane (piano) - comp on 2 and 4 with tension
piano_notes = [
    # A7 on beat 1 (4.5s)
    (4.5, 69), (4.5, 76), (4.5, 78), (4.5, 74),
    # Rest on beat 2
    # A7 on beat 3 (5.25s)
    (5.25, 69), (5.25, 76), (5.25, 78), (5.25, 74),
    # Rest on beat 4
]
for t, pitch in piano_notes:
    piano_program.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25))

# Dante (sax) - final resolution
# Motif variation: C - D - G - A (with space)
sax_notes = [
    (4.5, 60),  # C
    (4.875, 62),  # D
    (5.25, 69),  # G
    (5.625, 71),  # A
]
for t, pitch in sax_notes:
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25))

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
