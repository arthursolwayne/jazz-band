
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.5, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeating notes
# D minor blues line in D (D, Eb, E, F, G, A, Bb)
bass_notes = [
    (62, 1.5, 0.5),    # D
    (63, 2.0, 0.5),    # Eb
    (64, 2.5, 0.5),    # E
    (65, 3.0, 0.5),    # F
    (67, 3.5, 0.5),    # G
    (69, 4.0, 0.5),    # A
    (68, 4.5, 0.5),    # Bb
    (67, 5.0, 0.5),    # G
    (69, 5.5, 0.5),    # A
    (62, 6.0, 0.5)     # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# D7, G7, C7, F7 chords
piano_notes = [
    # Bar 2
    (67, 1.5, 0.25),  # D
    (72, 1.5, 0.25),  # G
    (74, 1.5, 0.25),  # B
    (69, 1.5, 0.25),  # F
    (72, 2.0, 0.25),  # G
    (76, 2.0, 0.25),  # B
    (79, 2.0, 0.25),  # D
    (74, 2.0, 0.25),  # B
    # Bar 3
    (67, 2.5, 0.25),  # D
    (72, 2.5, 0.25),  # G
    (74, 2.5, 0.25),  # B
    (69, 2.5, 0.25),  # F
    (72, 3.0, 0.25),  # G
    (76, 3.0, 0.25),  # B
    (79, 3.0, 0.25),  # D
    (74, 3.0, 0.25),  # B
    # Bar 4
    (67, 3.5, 0.25),  # D
    (72, 3.5, 0.25),  # G
    (74, 3.5, 0.25),  # B
    (69, 3.5, 0.25),  # F
    (72, 4.0, 0.25),  # G
    (76, 4.0, 0.25),  # B
    (79, 4.0, 0.25),  # D
    (74, 4.0, 0.25),  # B
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# You: Tenor sax. One short motif, make it sing.
# Motif: D - Eb - G - A (D minor)
# Start on 1.5s, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.5),    # D
    (63, 2.0, 0.5),    # Eb
    (67, 2.5, 0.5),    # G
    (69, 3.0, 0.5),    # A
    (62, 3.5, 0.5),    # D (repeat motif)
    (63, 4.0, 0.5),    # Eb
    (67, 4.5, 0.5),    # G
    (69, 5.0, 0.5),    # A
    (62, 5.5, 0.5),    # D (finish it)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add more fills for Little Ray in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (38, start + 0.75, 0.375), # Snare on 2
        (42, start, 0.1875), # Hihat on 1
        (42, start + 0.1875, 0.1875), # Hihat on &
        (42, start + 0.375, 0.1875), # Hihat on 2
        (42, start + 0.5625, 0.1875), # Hihat on &
        (42, start + 0.75, 0.1875), # Hihat on 3
        (42, start + 0.9375, 0.1875), # Hihat on &
        (42, start + 1.125, 0.1875), # Hihat on 4
        (36, start + 1.5, 0.375),  # Kick on 3
        (38, start + 1.5, 0.375),  # Snare on 4
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
