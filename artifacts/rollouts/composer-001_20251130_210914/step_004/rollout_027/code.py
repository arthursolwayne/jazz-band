
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, Dm7
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375),
    (65, 4.5, 0.375), (67, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (67, 1.875, 0.375), (64, 1.875, 0.375), (69, 1.875, 0.375),
    (62, 3.375, 0.375), (67, 3.375, 0.375), (64, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 3
    (62, 4.875, 0.375), (67, 4.875, 0.375), (64, 4.875, 0.375), (69, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat = [pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875) for i in range(8)]
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.extend(hihat)

# Sax: Motif in Dm, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    # Bar 3: Leave it hanging
    (65, 3.0, 0.375), (62, 3.375, 0.375),
    # Bar 4: Come back and finish it
    (67, 4.5, 0.375), (65, 4.875, 0.375), (64, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
