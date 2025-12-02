
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (42, 0.1875, 0.1875), # Hihat on 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (42, 0.5625, 0.1875),# Hihat on 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (42, 0.9375, 0.1875),# Hihat on 4
    (38, 1.125, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (38, 1.5, 0.375),    # F (root)
    (43, 1.875, 0.375),  # C (fifth)
    (37, 2.25, 0.375),   # E (chromatic approach)
    (38, 2.625, 0.375),  # F (root)

    # Bar 3 (3.0 - 4.5s)
    (43, 3.0, 0.375),    # C (fifth)
    (38, 3.375, 0.375),  # F (root)
    (40, 3.75, 0.375),   # A (chromatic approach)
    (43, 4.125, 0.375),  # C (fifth)

    # Bar 4 (4.5 - 6.0s)
    (38, 4.5, 0.375),    # F (root)
    (43, 4.875, 0.375),  # C (fifth)
    (37, 5.25, 0.375),   # E (chromatic approach)
    (38, 5.625, 0.375)   # F (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5, 0.375),    # F
    (69, 1.5, 0.375),    # A
    (72, 1.5, 0.375),    # C
    (76, 1.5, 0.375),    # E

    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 3.0, 0.375),    # G
    (71, 3.0, 0.375),    # Bb
    (74, 3.0, 0.375),    # D
    (76, 3.0, 0.375),    # F

    # Bar 4: C7 (C, E, G, Bb)
    (72, 4.5, 0.375),    # C
    (76, 4.5, 0.375),    # E
    (79, 4.5, 0.375),    # G
    (71, 4.5, 0.375)     # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it)
# Motif: F - Bb - F (Bar 2, first two notes), then Bb - F (Bar 4, second two notes)
sax_notes = [
    (72, 1.5, 0.375),    # F
    (77, 1.875, 0.375),  # Bb
    (72, 4.5, 0.375),    # F
    (77, 4.875, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Little Ray in Bars 2-4 (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625))
    # Hi-hat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
