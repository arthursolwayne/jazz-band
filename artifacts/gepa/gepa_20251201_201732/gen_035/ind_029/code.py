
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # F (root)
    (47, 1.875, 0.375),  # Ab (chromatic approach)
    (44, 2.25, 0.375),  # C (fifth)
    (46, 2.625, 0.375),  # Bb (chromatic approach)
    (45, 3.0, 0.375),  # F
    (47, 3.375, 0.375),  # Ab
    (44, 3.75, 0.375),  # C
    (46, 4.125, 0.375),  # Bb
    (49, 4.5, 0.375),  # D (root of next chord)
    (51, 4.875, 0.375),  # E (chromatic approach)
    (48, 5.25, 0.375),  # G (fifth)
    (50, 5.625, 0.375),  # F# (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (53, 1.5, 0.375),  # F
    (58, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (57, 2.25, 0.375),  # Bb
    (62, 2.25, 0.375),  # D
    (60, 2.25, 0.375),  # F
    (65, 2.25, 0.375),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (60, 3.0, 0.375),  # C
    (63, 3.0, 0.375),  # Eb
    (67, 3.0, 0.375),  # G
    (65, 3.0, 0.375),  # Bb
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (intervallic: 4 - 3 - 4)
sax_notes = [
    (60, 1.5, 0.375),  # F
    (65, 1.875, 0.375),  # Bb
    (62, 2.25, 0.375),  # C
    (60, 2.625, 0.375),  # F (start of motif)
    (60, 3.0, 0.375),  # F (repeat)
    (65, 3.375, 0.375),  # Bb
    (62, 3.75, 0.375),  # C
    (60, 4.125, 0.375),  # F (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, bar_start, 0.375),  # Kick on 1
        (42, bar_start, 0.375),  # Hihat on 1
        (38, bar_start + 0.375, 0.375),  # Snare on 2
        (42, bar_start + 0.375, 0.375),  # Hihat on 2
        (36, bar_start + 0.75, 0.375),  # Kick on 3
        (42, bar_start + 0.75, 0.375),  # Hihat on 3
        (38, bar_start + 1.125, 0.375),  # Snare on 4
        (42, bar_start + 1.125, 0.375),  # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
