
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

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.375, 0.75), # Hihat on 2
    (36, 0.75, 1.0),  # Kick on 3
    (42, 1.125, 1.5)  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Drums - Bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Add to drums
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bass - Bars 2-4 (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: D (2) -> F# (4) -> D (2) -> E (3) (chromatic approach)
    (43, 1.5, 0.375),  # D2
    (46, 1.875, 0.375), # F#2
    (43, 2.25, 0.375),  # D2
    (44, 2.625, 0.375), # E2

    # Bar 3: A (5) -> C# (7) -> A (5) -> B (6)
    (47, 2.875, 0.375), # A2
    (50, 3.25, 0.375),  # C#2
    (47, 3.625, 0.375), # A2
    (48, 4.0, 0.375),   # B2

    # Bar 4: D (2) -> F# (4) -> D (2) -> C# (3) (chromatic approach)
    (43, 4.25, 0.375),  # D2
    (46, 4.625, 0.375), # F#2
    (43, 5.0, 0.375),   # D2
    (45, 5.375, 0.375)  # C#2
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano - Bars 2-4 (Open voicings, different chords each bar, resolve on the last)
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    (43, 1.5, 0.375),  # D2
    (46, 1.5, 0.375),  # F#2
    (47, 1.5, 0.375),  # A2
    (40, 1.5, 0.375),  # C2
    (53, 1.5, 0.375),  # D4
    (56, 1.5, 0.375),  # F#4
    (57, 1.5, 0.375),  # A4
    (50, 1.5, 0.375)   # C4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    (47, 2.25, 0.375),  # G2
    (50, 2.25, 0.375),  # B2
    (43, 2.25, 0.375),  # D2
    (46, 2.25, 0.375),  # F2
    (60, 2.25, 0.375),  # G4
    (63, 2.25, 0.375),  # B4
    (56, 2.25, 0.375),  # D4
    (59, 2.25, 0.375)   # F4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    (43, 4.25, 0.375),  # D2
    (46, 4.25, 0.375),  # F#2
    (47, 4.25, 0.375),  # A2
    (45, 4.25, 0.375),  # C#2
    (53, 4.25, 0.375),  # D4
    (56, 4.25, 0.375),  # F#4
    (57, 4.25, 0.375),  # A4
    (54, 4.25, 0.375)   # C#4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax - Bars 2-4 (One short motif, make it sing)
# Motif: D4 - F#4 - A4 - D5 (hanging on D5)
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375), # F#4
    (67, 2.25, 0.375),  # A4
    (69, 2.625, 0.375), # D5 (hanging)
    (67, 2.625, 0.375), # A4
    (65, 2.625, 0.375), # F#4
    (62, 2.625, 0.375)  # D4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
