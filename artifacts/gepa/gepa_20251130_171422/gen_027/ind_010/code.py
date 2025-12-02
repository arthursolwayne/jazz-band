
import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36   # Kick drum
snare = 38  # Snare drum
hihat = 42  # Hi-hat

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (kick, 0.0), (hihat, 0.375), (hihat, 0.75), (hihat, 1.125),
    (snare, 1.5), (hihat, 1.875), (hihat, 2.25), (hihat, 2.625),
    (kick, 3.0), (hihat, 3.375), (hihat, 3.75), (hihat, 4.125),
    (snare, 4.5), (hihat, 4.875), (hihat, 5.25), (hihat, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line with chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (46, 2.25),  # Bb -> B -> A -> B
    (47, 2.5), (46, 2.75), (45, 3.0), (44, 3.25)   # C -> B -> Bb -> A
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat (1.75s): F7 (F, A, C, E)
    (65, 1.75), (67, 1.75), (69, 1.75), (72, 1.75),  # F, A, C, E
    # 4th beat (2.25s): Bb7 (Bb, D, F, Ab)
    (62, 2.25), (64, 2.25), (67, 2.25), (69, 2.25)   # Bb, D, F, Ab
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Short motif in F (F, G, Ab, Bb)
# Start at 1.5s, play F (65), G (67), Ab (69), Bb (71)
# End at 2.0s, leave it hanging — come back at 4.5s to finish it
sax_notes = [
    (65, 1.5), (67, 1.75), (69, 2.0), (71, 2.125),  # Start the motif
    (65, 4.5), (67, 4.75), (69, 5.0), (71, 5.125)   # Finish the motif
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line with chromatic approaches
bass_notes = [
    (44, 3.0), (45, 3.25), (43, 3.5), (45, 3.75),  # A -> Bb -> G -> Bb
    (46, 4.0), (45, 4.25), (44, 4.5), (43, 4.75)   # B -> Bb -> A -> G
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat (3.25s): F7 (F, A, C, E)
    (65, 3.25), (67, 3.25), (69, 3.25), (72, 3.25),  # F, A, C, E
    # 4th beat (3.75s): Bb7 (Bb, D, F, Ab)
    (62, 3.75), (64, 3.75), (67, 3.75), (69, 3.75)   # Bb, D, F, Ab
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: Continue the same pattern
drum_notes = [
    (kick, 3.0), (hihat, 3.375), (hihat, 3.75), (hihat, 4.125),
    (snare, 4.5), (hihat, 4.875), (hihat, 5.25), (hihat, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line with chromatic approaches
bass_notes = [
    (43, 4.5), (44, 4.75), (42, 5.0), (44, 5.25),  # G -> A -> F -> A
    (45, 5.5), (44, 5.75), (43, 6.0), (42, 6.25)   # Bb -> A -> G -> F
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat (4.75s): F7 (F, A, C, E)
    (65, 4.75), (67, 4.75), (69, 4.75), (72, 4.75),  # F, A, C, E
    # 4th beat (5.25s): Bb7 (Bb, D, F, Ab)
    (62, 5.25), (64, 5.25), (67, 5.25), (69, 5.25)   # Bb, D, F, Ab
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: Continue the same pattern
drum_notes = [
    (kick, 4.5), (hihat, 4.875), (hihat, 5.25), (hihat, 5.625),
    (snare, 6.0), (hihat, 6.375), (hihat, 6.75), (hihat, 7.125)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.writeFile("dante_intro.mid")
