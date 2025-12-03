
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
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.375, 0.75), # Hihat on 2
    (38, 0.75, 1.0),  # Snare on 3
    (42, 1.125, 1.5)  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (37, 1.5, 1.5),   # F (root)
    (40, 1.875, 2.25), # Ab (fifth, chromatic approach)
    (38, 2.25, 2.625), # G (chromatic)
    (37, 2.625, 3.0),  # F (root)
    (39, 3.0, 3.375),  # A (chromatic)
    (41, 3.375, 3.75), # Bb (fifth)
    (40, 3.75, 4.125), # Ab (fifth)
    (37, 4.125, 4.5),  # F (root)
    (39, 4.5, 4.875),  # A (chromatic)
    (41, 4.875, 5.25), # Bb (fifth)
    (40, 5.25, 5.625), # Ab (fifth)
    (37, 5.625, 6.0)   # F (root)
]
for note, start, end in bass_notes:
    b = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(b)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2 (Fm7)
    (48, 1.5, 1.5), (52, 1.5, 1.5), (53, 1.5, 1.5), (55, 1.5, 1.5),
    # Bar 3 (Bb7)
    (53, 2.25, 2.25), (57, 2.25, 2.25), (60, 2.25, 2.25), (62, 2.25, 2.25),
    # Bar 4 (Ab7)
    (55, 3.0, 3.0), (59, 3.0, 3.0), (62, 3.0, 3.0), (64, 3.0, 3.0),
    # Comp on 2 and 4
    (51, 2.625, 2.75), (55, 2.625, 2.75), (57, 2.625, 2.75), # 2
    (51, 4.5, 4.625), (55, 4.5, 4.625), (57, 4.5, 4.625)   # 4
]
for note, start, end in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(p)

# Sax: Motif with tension and release
# Motif: F - Ab - G - F (staccato)
# Repeat with variation: Ab - Bb - A - G
sax_notes = [
    (37, 1.5, 1.625), (40, 1.625, 1.75), (39, 1.75, 1.875), (37, 1.875, 2.0),
    (40, 2.25, 2.375), (43, 2.375, 2.5), (41, 2.5, 2.625), (39, 2.625, 2.75),
    (37, 3.0, 3.125), (40, 3.125, 3.25), (39, 3.25, 3.375), (37, 3.375, 3.5),
    (40, 3.75, 3.875), (43, 3.875, 4.0), (41, 4.0, 4.125), (39, 4.125, 4.25),
    (37, 4.5, 4.625), (40, 4.625, 4.75), (39, 4.75, 4.875), (37, 4.875, 5.0),
    (40, 5.25, 5.375), (43, 5.375, 5.5), (41, 5.5, 5.625), (39, 5.625, 5.75),
    (37, 6.0, 6.125)
]
for note, start, end in sax_notes:
    s = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(s)

# Drums: Full pattern for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 2
    if bar == 2:
        # Kick on 1
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
        drums.notes.append(dr)
        # Snare on 2
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
        drums.notes.append(dr)
        # Kick on 3
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
        drums.notes.append(dr)
        # Snare on 4
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
        drums.notes.append(dr)
    # Bar 3
    elif bar == 3:
        # Kick on 1
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
        drums.notes.append(dr)
        # Snare on 2
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
        drums.notes.append(dr)
        # Kick on 3
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
        drums.notes.append(dr)
        # Snare on 4
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
        drums.notes.append(dr)
    # Bar 4
    elif bar == 4:
        # Kick on 1
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
        drums.notes.append(dr)
        # Snare on 2
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
        drums.notes.append(dr)
        # Kick on 3
        dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
        drums.notes.append(dr)
        # Snare on 4
        dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
        drums.notes.append(dr)

# Add hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(0, 4):
        dr = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.25)
        drums.notes.append(dr)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
