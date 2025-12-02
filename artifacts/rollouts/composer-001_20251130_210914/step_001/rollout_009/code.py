
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (44, 2.25, 0.375), (43, 2.625, 0.375),  # Bar 2
    (45, 3.0, 0.375), (46, 3.375, 0.375), (44, 3.75, 0.375), (43, 4.125, 0.375),  # Bar 3
    (45, 4.5, 0.375), (46, 4.875, 0.375), (44, 5.25, 0.375), (43, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    (57, 1.875, 0.375), (60, 1.875, 0.375), (64, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 3 (3.0 - 4.5)
    (57, 3.375, 0.375), (60, 3.375, 0.375), (64, 3.375, 0.375), (62, 3.375, 0.375),
    # Bar 4 (4.5 - 6.0)
    (57, 4.875, 0.375), (60, 4.875, 0.375), (64, 4.875, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Saxophone - short motif, starts in bar 2, leaves it hanging, returns in bar 4
sax_notes = [
    # Bar 2: Start motif
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    # Bar 3: Silence, leave it hanging
    # Bar 4: Return to finish motif
    (62, 4.5, 0.375), (65, 4.875, 0.375), (67, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    for kick in [0.0, 0.75]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + kick, end=start + kick + 0.375))
    # Snare on 2 and 4
    for snare in [0.375, 1.125]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + snare, end=start + snare + 0.375))
    # Hihat on every eighth
    for hihat in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + hihat, end=start + hihat + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
