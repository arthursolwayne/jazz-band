
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
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375), (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375), (38, 1.875, 0.375),
    # Hihat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375), # D
    (63, 1.875, 0.375), # Eb
    (60, 2.25, 0.375), # Bb
    (62, 2.625, 0.375), # D
    (64, 3.0, 0.375), # F
    (62, 3.375, 0.375), # D
    (61, 3.75, 0.375), # C
    (62, 4.125, 0.375), # D
    (64, 4.5, 0.375), # F
    (65, 4.875, 0.375), # G
    (62, 5.25, 0.375), # D
    (63, 5.625, 0.375), # Eb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (62, 2.25, 0.375), # D
    (67, 2.25, 0.375), # G
    (64, 2.25, 0.375), # Bb
    (69, 2.25, 0.375), # C
    # Bar 3: Dm7 on beat 2
    (62, 3.75, 0.375), # D
    (67, 3.75, 0.375), # G
    (64, 3.75, 0.375), # Bb
    (69, 3.75, 0.375), # C
    # Bar 4: Dm7 on beat 2
    (62, 5.25, 0.375), # D
    (67, 5.25, 0.375), # G
    (64, 5.25, 0.375), # Bb
    (69, 5.25, 0.375), # C
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = (36, bar_start, bar_start + 0.375)
    kick2 = (36, bar_start + 1.125, bar_start + 1.5)
    # Snare on 2 and 4
    snare1 = (38, bar_start + 0.75, bar_start + 1.125)
    snare2 = (38, bar_start + 1.875, bar_start + 2.25)
    # Hihat on every eighth
    hihat_notes = [
        (42, bar_start + i * 0.375, bar_start + i * 0.375 + 0.1875) for i in range(8)
    ]
    for note in [kick1, kick2, snare1, snare2] + hihat_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    (64, 1.5, 0.5), # D (start of motif)
    (66, 2.0, 0.5), # F
    (64, 2.5, 0.5), # D
    (62, 3.0, 0.5), # Bb
    (64, 3.5, 0.5), # D
    (66, 4.0, 0.5), # F
    (64, 4.5, 0.5), # D
    (62, 5.0, 0.5), # Bb
    (64, 5.5, 0.5)  # D (ending)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
