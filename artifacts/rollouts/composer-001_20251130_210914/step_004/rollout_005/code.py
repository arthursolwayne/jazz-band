
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

# Bars 2-4 (1.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.875), (61, 2.25), (60, 2.625),  # Dm7
    (62, 2.625), (63, 2.875), (61, 3.25), (60, 3.625), # Dm7
    (62, 3.625), (63, 3.875), (61, 4.25), (60, 4.625), # Dm7
    (62, 4.625), (63, 4.875), (61, 5.25), (60, 5.625)  # Dm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875), (67, 1.875), (60, 1.875), (72, 1.875),  # Dm7
    (62, 2.625), (67, 2.625), (60, 2.625), (72, 2.625),  # Dm7
    # Bar 3
    (62, 3.875), (67, 3.875), (60, 3.875), (72, 3.875),  # Dm7
    (62, 4.625), (67, 4.625), (60, 4.625), (72, 4.625)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging, come back and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> Eb -> F -> D (hanging), then G -> A -> Bb -> C
sax_notes = [
    (62, 1.5), (63, 1.875), (65, 2.25), (62, 2.625),   # D -> Eb -> F -> D
    (67, 3.0), (69, 3.375), (70, 3.75), (71, 4.125)    # G -> A -> Bb -> C
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
