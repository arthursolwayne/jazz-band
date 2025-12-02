
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
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in D minor, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),  # Dm7: D, F, Eb, G
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),  # G7: G, B, A, D
    (62, 4.5), (64, 4.875), (63, 5.25), (65, 5.625)   # Dm7 again
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane - 7th chords, comp on 2 and 4
# Dm7: D F Ab C
# G7: G B D F
piano_notes = [
    # Bar 2
    (62, 2.0), (65, 2.0), (67, 2.0), (71, 2.0),  # Dm7
    (67, 3.0), (71, 3.0), (69, 3.0), (72, 3.0),  # G7
    # Bar 3
    (62, 4.0), (65, 4.0), (67, 4.0), (71, 4.0),  # Dm7
    (67, 5.0), (71, 5.0), (69, 5.0), (72, 5.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Tenor Sax: One short motif, make it sing
# Start on D (62), build tension with chromatic passing tones
sax_notes = [
    (62, 1.5), (63, 1.75), (62, 2.0),  # D -> Eb -> D
    (64, 2.25), (65, 2.5), (64, 2.75),  # F -> G -> F
    (63, 3.0), (62, 3.25), (63, 3.5)   # Eb -> D -> Eb (hanging)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
