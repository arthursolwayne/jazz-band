
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in F, chromatic approaches
# F Dorian: F, G, A, Bb, C, D, Eb
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (52, 2.625),  # F -> Eb -> D -> F
    (53, 2.75), (51, 3.125), (50, 3.5), (52, 3.875),  # F -> Eb -> D -> F
    (53, 4.0), (51, 4.375), (50, 4.75), (52, 5.125),  # F -> Eb -> D -> F
    (53, 5.25), (51, 5.625), (50, 6.0), (52, 6.375)   # F -> Eb -> D -> F
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
# F7, Bb7, C7, D7
piano_notes = [
    (64, 2.0), (67, 2.0), (69, 2.0), (60, 2.0),  # F7
    (64, 3.0), (67, 3.0), (69, 3.0), (60, 3.0),  # F7
    (64, 4.0), (67, 4.0), (69, 4.0), (60, 4.0),  # F7
    (64, 5.0), (67, 5.0), (69, 5.0), (60, 5.0)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante on sax: One short motif that sings
# F -> Eb -> D -> C (chromatic descent)
sax_notes = [
    (65, 1.5), (64, 1.75), (63, 2.0), (60, 2.25),  # F -> Eb -> D -> C
    (65, 2.5), (64, 2.75), (63, 3.0), (60, 3.25),  # F -> Eb -> D -> C
    (65, 3.5), (64, 3.75), (63, 4.0), (60, 4.25),  # F -> Eb -> D -> C
    (65, 4.5), (64, 4.75), (63, 5.0), (60, 5.25)   # F -> Eb -> D -> C
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.125)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.875)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.25)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.625)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.0)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
