
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),# Hihat on &1
    (42, 0.25, 0.125), # Hihat on 2
    (42, 0.375, 0.125),# Hihat on &2
    (42, 0.5, 0.125),  # Hihat on 3
    (42, 0.625, 0.125),# Hihat on &3
    (42, 0.75, 0.125), # Hihat on 4
    (42, 0.875, 0.125),# Hihat on &4
    (36, 1.125, 0.375),# Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Marcus: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2
    (40, 1.875, 0.375), # E2 (chromatic approach)
    (43, 2.25, 0.375),  # G2
    (41, 2.625, 0.375), # F#2 (chromatic approach)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (65, 1.5, 0.375),  # F4
    (69, 1.5, 0.375),  # A4
    (67, 1.5, 0.375),  # C5
    (70, 1.5, 0.375),  # E5
    (72, 1.875, 0.375),# G5 (resolve)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0 - 4.5s)
# Diane: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (60, 3.0, 0.375),  # C4
    (63, 3.0, 0.375),  # Eb4
    (67, 3.0, 0.375),  # G4
    (62, 3.0, 0.375),  # Bb4
    (69, 3.375, 0.375),# A4 (resolve)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4 (4.5 - 6.0s)
# Diane: Dm7 (D, F, A, C)
piano_notes = [
    (62, 4.5, 0.375),  # D4
    (65, 4.5, 0.375),  # F4
    (67, 4.5, 0.375),  # A4
    (67, 4.5, 0.375),  # C5 (octave)
    (69, 4.875, 0.375),# A4 (resolve)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 (65), Ab4 (68), Bb4 (62), F5 (77) - 4 notes over 2 bars

# Bar 2: Play first two notes (F, Ab), leave it hanging
sax_notes = [
    (65, 1.5, 0.375),  # F4
    (68, 1.875, 0.375), # Ab4
]

# Bar 3: Play Bb4, leave it hanging
sax_notes.append((62, 3.0, 0.375))  # Bb4

# Bar 4: Play F5 (resolve)
sax_notes.append((77, 4.5, 0.375))  # F5

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start + 0.0, 0.375),  # Kick on 1
        (38, bar_start + 0.75, 0.375), # Snare on 2
        (42, bar_start + 0.0, 0.125),  # Hihat on 1
        (42, bar_start + 0.125, 0.125),# Hihat on &1
        (42, bar_start + 0.25, 0.125), # Hihat on 2
        (42, bar_start + 0.375, 0.125),# Hihat on &2
        (42, bar_start + 0.5, 0.125),  # Hihat on 3
        (42, bar_start + 0.625, 0.125),# Hihat on &3
        (42, bar_start + 0.75, 0.125), # Hihat on 4
        (42, bar_start + 0.875, 0.125),# Hihat on &4
        (36, bar_start + 1.125, 0.375),# Kick on 3
        (38, bar_start + 1.5, 0.375),  # Snare on 4
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
