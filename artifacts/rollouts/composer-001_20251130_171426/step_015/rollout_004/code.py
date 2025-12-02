
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (30, 1.5, 0.375), (32, 1.875, 0.375), (31, 2.25, 0.375), (30, 2.625, 0.375),
    (28, 2.625, 0.375), (30, 3.0, 0.375), (32, 3.375, 0.375), (31, 3.75, 0.375),
    (30, 4.125, 0.375), (28, 4.5, 0.375), (30, 4.875, 0.375), (32, 5.25, 0.375),
    (31, 5.625, 0.375), (30, 6.0, 0.375),
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (64, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875), (71, 1.875, 0.1875),
    # Bar 3: Fm7 on beat 2
    (64, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875), (71, 3.375, 0.1875),
    # Bar 4: Fm7 on beat 2
    (64, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875), (71, 4.875, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = (36, start, 0.375)
    kick3 = (36, start + 0.75, 0.375)
    # Snare on 2 and 4
    snare2 = (38, start + 0.375, 0.375)
    snare4 = (38, start + 1.125, 0.375)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = (42, start + i * 0.1875, 0.1875)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat[0], start=hihat[1], end=hihat[2]))
    # Add kick and snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick1[0], start=kick1[1], end=kick1[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick3[0], start=kick3[1], end=kick3[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare2[0], start=snare2[1], end=snare2[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare4[0], start=snare4[1], end=snare4[2]))

# Saxophone - short motif, start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Motif: F - Ab - Bb - (rest)
# Then: F - Ab - Bb - C (resolve)

sax_notes = [
    (65, 1.5, 0.375), (68, 1.875, 0.375), (67, 2.25, 0.375), (67, 2.625, 0.375),
    (65, 2.625, 0.375), (68, 2.625, 0.375), (67, 2.625, 0.375), (69, 3.0, 0.375),
    (67, 3.375, 0.375), (65, 3.75, 0.375), (68, 4.125, 0.375), (69, 4.5, 0.375),
    (71, 4.875, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
