
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.375), (38, 3.75), (42, 3.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking bass line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (42, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (42, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 1 (no chord), then Bb7 on beat 2
    (71, 1.75), (74, 1.75), (77, 1.75), (79, 1.75),
    # Bar 2: E7 on beat 4
    (76, 2.75), (79, 2.75), (81, 2.75), (84, 2.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: motif in F, singing, leave it hanging
sax_notes = [
    (65, 1.5), (67, 1.75), (68, 2.0),
    (67, 2.25), (65, 2.5), (63, 2.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking bass line in F, chromatic approaches
bass_notes = [
    (45, 3.0), (46, 3.25), (44, 3.5), (42, 3.75),
    (45, 4.0), (46, 4.25), (44, 4.5), (42, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 1 (no chord), then Bb7 on beat 2
    (71, 3.25), (74, 3.25), (77, 3.25), (79, 3.25),
    # Bar 3: E7 on beat 4
    (76, 4.25), (79, 4.25), (81, 4.25), (84, 4.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: motif continuation
sax_notes = [
    (65, 3.0), (67, 3.25), (68, 3.5),
    (67, 3.75), (65, 4.0), (63, 4.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking bass line in F, chromatic approaches
bass_notes = [
    (45, 4.5), (46, 4.75), (44, 5.0), (42, 5.25),
    (45, 5.5), (46, 5.75), (44, 6.0), (42, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 1 (no chord), then Bb7 on beat 2
    (71, 4.75), (74, 4.75), (77, 4.75), (79, 4.75),
    # Bar 4: E7 on beat 4
    (76, 5.75), (79, 5.75), (81, 5.75), (84, 5.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: motif resolution
sax_notes = [
    (65, 4.5), (67, 4.75), (68, 5.0),
    (67, 5.25), (65, 5.5), (64, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.625), (38, 5.999), (42, 5.999)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
