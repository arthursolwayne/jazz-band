
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5), (64, 1.875), (60, 2.25), (62, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass walking line in Dm (F, Ab, D, C)
bass_notes = [
    (65, 1.5), (63, 1.875), (62, 2.25), (60, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (62, 1.875), (67, 1.875), (65, 1.875), (64, 1.875),
    # Bar 3: G7 on beat 4
    (67, 2.625), (71, 2.625), (69, 2.625), (68, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continuation
sax_notes = [
    (60, 3.0), (62, 3.375), (64, 3.75), (62, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass walking line in Dm (F, Ab, D, C)
bass_notes = [
    (63, 3.0), (62, 3.375), (60, 3.75), (62, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3: Dm7 on beat 2
    (62, 3.375), (67, 3.375), (65, 3.375), (64, 3.375),
    # Bar 4: G7 on beat 4
    (67, 4.125), (71, 4.125), (69, 4.125), (68, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody continuation
sax_notes = [
    (62, 4.5), (64, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass walking line in Dm (F, Ab, D, C)
bass_notes = [
    (62, 4.5), (60, 4.875), (62, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4: Dm7 on beat 2
    (62, 4.875), (67, 4.875), (65, 4.875), (64, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
