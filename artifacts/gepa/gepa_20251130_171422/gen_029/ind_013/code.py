
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
    (36, 0.0), (38, 0.375), (42, 0.1875),
    (36, 0.75), (38, 1.125), (42, 0.9375),
    (36, 1.5), (38, 1.875), (42, 1.6875),
    (36, 2.25), (38, 2.625), (42, 2.4375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Sax enters with a sparse motif (1.5 - 3.0s)
sax_notes = [
    (62, 1.5), (65, 1.75), (62, 2.0), (64, 2.25), (62, 2.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass enters with a walking line (1.5 - 3.0s)
bass_notes = [
    (62, 1.5), (64, 1.75), (63, 2.0), (67, 2.25), (65, 2.5), (67, 2.75), (66, 3.0), (64, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano enters with 7th chords on beat 2 and 4 (1.5 - 3.0s)
piano_notes = [
    (71, 1.75), (74, 1.75), (72, 1.75), (69, 1.75),  # C7 (7th chord)
    (71, 2.25), (74, 2.25), (72, 2.25), (69, 2.25),  # C7 (7th chord)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Continue the motif, develop it (3.0 - 4.5s)
sax_notes = [
    (64, 3.0), (62, 3.25), (65, 3.5), (62, 3.75), (64, 4.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass continues walking line (3.0 - 4.5s)
bass_notes = [
    (64, 3.0), (66, 3.25), (65, 3.5), (68, 3.75), (66, 4.0), (68, 4.25), (67, 4.5), (65, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano continues with 7th chords on beat 2 and 4 (3.0 - 4.5s)
piano_notes = [
    (71, 3.25), (74, 3.25), (72, 3.25), (69, 3.25),  # C7 (7th chord)
    (71, 3.75), (74, 3.75), (72, 3.75), (69, 3.75),  # C7 (7th chord)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 4: Sax finishes the motif and resolves (4.5 - 6.0s)
sax_notes = [
    (62, 4.5), (64, 4.75), (62, 5.0), (65, 5.25), (62, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass continues walking line (4.5 - 6.0s)
bass_notes = [
    (65, 4.5), (67, 4.75), (66, 5.0), (69, 5.25), (67, 5.5), (69, 5.75), (68, 6.0), (66, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano continues with 7th chords on beat 2 and 4 (4.5 - 6.0s)
piano_notes = [
    (71, 4.75), (74, 4.75), (72, 4.75), (69, 4.75),  # C7 (7th chord)
    (71, 5.25), (74, 5.25), (72, 5.25), (69, 5.25),  # C7 (7th chord)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums continue groove (4.5 - 6.0s)
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.6875),
    (36, 5.25), (38, 5.625), (42, 5.4375),
    (36, 6.0), (38, 6.375), (42, 6.1875),
    (36, 6.75), (38, 7.125), (42, 6.9375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
