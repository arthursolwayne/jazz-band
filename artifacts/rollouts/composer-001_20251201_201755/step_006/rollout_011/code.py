
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line (Marcus): Roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),  # G2 (Fm root + 5)
    (40, 1.875, 0.375), # D2 (Fm root)
    (43, 2.25, 0.375),  # G2 (Fm root + 5)
    (40, 2.625, 0.375), # D2 (Fm root)
    (39, 3.0, 0.375),   # C2 (chromatic approach)
    (43, 3.375, 0.375), # G2 (Fm root + 5)
    (40, 3.75, 0.375),  # D2 (Fm root)
    (43, 4.125, 0.375), # G2 (Fm root + 5)
    (40, 4.5, 0.375),   # D2 (Fm root)
    (39, 4.875, 0.375), # C2 (chromatic approach)
    (43, 5.25, 0.375),  # G2 (Fm root + 5)
    (40, 5.625, 0.375)  # D2 (Fm root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 0.375),  # F
    (60, 1.5, 0.375),  # Ab
    (65, 1.5, 0.375),  # C
    (67, 1.5, 0.375),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 0.375), # Bb
    (62, 2.25, 0.375), # D
    (53, 2.25, 0.375), # F
    (60, 2.25, 0.375), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (56, 3.0, 0.375),  # Eb
    (60, 3.0, 0.375),  # G
    (58, 3.0, 0.375),  # Bb
    (67, 3.0, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * (bar - 1)
    # Bar 2
    if bar == 2:
        drum_notes = [
            (36, start, 0.375),   # Kick on 1
            (42, start, 0.375),   # Hihat on 1
            (38, start + 0.375, 0.375), # Snare on 2
            (42, start + 0.375, 0.375), # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375), # Snare on 4
            (42, start + 1.125, 0.375)  # Hihat on 4
        ]
    # Bar 3
    elif bar == 3:
        drum_notes = [
            (36, start, 0.375),   # Kick on 1
            (42, start, 0.375),   # Hihat on 1
            (38, start + 0.375, 0.375), # Snare on 2
            (42, start + 0.375, 0.375), # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375), # Snare on 4
            (42, start + 1.125, 0.375)  # Hihat on 4
        ]
    # Bar 4
    elif bar == 4:
        drum_notes = [
            (36, start, 0.375),   # Kick on 1
            (42, start, 0.375),   # Hihat on 1
            (38, start + 0.375, 0.375), # Snare on 2
            (42, start + 0.375, 0.375), # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375), # Snare on 4
            (42, start + 1.125, 0.375)  # Hihat on 4
        ]
    for note, start_time, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm harmony)
sax_notes = [
    (53, 1.5, 0.375),   # F
    (60, 1.875, 0.375), # Ab
    (58, 2.25, 0.375),  # Bb
    (53, 2.625, 0.375), # F (end of bar 2)
    (53, 3.0, 0.375),   # F (start of bar 3)
    (60, 3.375, 0.375), # Ab
    (58, 3.75, 0.375),  # Bb
    (53, 4.125, 0.375), # F (end of bar 3)
    (53, 4.5, 0.375),   # F (start of bar 4)
    (60, 4.875, 0.375), # Ab
    (58, 5.25, 0.375),  # Bb
    (53, 5.625, 0.375)  # F (end of bar 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
