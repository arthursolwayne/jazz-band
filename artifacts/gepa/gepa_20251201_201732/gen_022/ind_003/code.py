
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 62, 100, 0.25),  # D2
    (1.75, 64, 100, 0.25),  # E2 (chromatic approach)
    (2.0, 62, 100, 0.25),  # D2
    (2.25, 67, 100, 0.25),  # A2 (fifth of D)
    (2.5, 67, 100, 0.25),  # A2
    (2.75, 69, 100, 0.25),  # B2 (chromatic approach)
    (3.0, 67, 100, 0.25),  # A2
    (3.25, 72, 100, 0.25),  # D3 (octave)
    (3.5, 72, 100, 0.25),  # D3
    (3.75, 74, 100, 0.25),  # E3 (chromatic approach)
    (4.0, 72, 100, 0.25),  # D3
    (4.25, 77, 100, 0.25),  # A3 (fifth of D)
    (4.5, 77, 100, 0.25),  # A3
    (4.75, 79, 100, 0.25),  # B3 (chromatic approach)
    (5.0, 77, 100, 0.25),  # A3
    (5.25, 82, 100, 0.25),  # D4 (octave)
]
for time, note, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    (1.5, 62, 100, 0.25),  # D
    (1.5, 67, 100, 0.25),  # A
    (1.5, 69, 100, 0.25),  # B
    (1.5, 72, 100, 0.25),  # D
    (1.75, 67, 100, 0.25),  # A
    (1.75, 72, 100, 0.25),  # D
    (1.75, 74, 100, 0.25),  # E
    (1.75, 76, 100, 0.25),  # G
    (2.0, 62, 100, 0.25),  # D
    (2.0, 67, 100, 0.25),  # A
    (2.0, 69, 100, 0.25),  # B
    (2.0, 72, 100, 0.25),  # D
    (2.25, 67, 100, 0.25),  # A
    (2.25, 72, 100, 0.25),  # D
    (2.25, 74, 100, 0.25),  # E
    (2.25, 76, 100, 0.25),  # G
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Bar 3: D7 (D, F#, A, C)
piano_notes = [
    (2.5, 62, 100, 0.25),  # D
    (2.5, 67, 100, 0.25),  # A
    (2.5, 69, 100, 0.25),  # B
    (2.5, 71, 100, 0.25),  # C
    (2.75, 67, 100, 0.25),  # A
    (2.75, 71, 100, 0.25),  # C
    (2.75, 74, 100, 0.25),  # E
    (2.75, 76, 100, 0.25),  # G
    (3.0, 62, 100, 0.25),  # D
    (3.0, 67, 100, 0.25),  # A
    (3.0, 69, 100, 0.25),  # B
    (3.0, 71, 100, 0.25),  # C
    (3.25, 67, 100, 0.25),  # A
    (3.25, 71, 100, 0.25),  # C
    (3.25, 74, 100, 0.25),  # E
    (3.25, 76, 100, 0.25),  # G
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    (3.5, 62, 100, 0.25),  # D
    (3.5, 65, 100, 0.25),  # F
    (3.5, 67, 100, 0.25),  # A
    (3.5, 72, 100, 0.25),  # D
    (3.75, 67, 100, 0.25),  # A
    (3.75, 72, 100, 0.25),  # D
    (3.75, 74, 100, 0.25),  # E
    (3.75, 76, 100, 0.25),  # G
    (4.0, 62, 100, 0.25),  # D
    (4.0, 65, 100, 0.25),  # F
    (4.0, 67, 100, 0.25),  # A
    (4.0, 72, 100, 0.25),  # D
    (4.25, 67, 100, 0.25),  # A
    (4.25, 72, 100, 0.25),  # D
    (4.25, 74, 100, 0.25),  # E
    (4.25, 76, 100, 0.25),  # G
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Phrase: D (62), F (65), B (69), D (72), [rest], D (62), F (65), B (69), D (72), [rest]
sax_notes = [
    (1.5, 62, 100, 0.25),  # D
    (1.75, 65, 100, 0.25),  # F
    (2.0, 69, 100, 0.25),  # B
    (2.25, 72, 100, 0.25),  # D
    (2.5, 62, 100, 0.25),  # D
    (2.75, 65, 100, 0.25),  # F
    (3.0, 69, 100, 0.25),  # B
    (3.25, 72, 100, 0.25),  # D
    (3.5, 62, 100, 0.25),  # D
    (3.75, 65, 100, 0.25),  # F
    (4.0, 69, 100, 0.25),  # B
    (4.25, 72, 100, 0.25),  # D
]
for time, note, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    if bar == 2:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.375, 42, 100),  # Hihat on 2
            (bar_start + 0.75, 38, 100),  # Snare on 3
            (bar_start + 1.125, 42, 100),  # Hihat on 4
            (bar_start + 1.5, 36, 100),  # Kick on 1
            (bar_start + 1.875, 42, 100),  # Hihat on 2
            (bar_start + 2.25, 38, 100),  # Snare on 3
            (bar_start + 2.625, 42, 100),  # Hihat on 4
        ]
    elif bar == 3:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.375, 42, 100),  # Hihat on 2
            (bar_start + 0.75, 38, 100),  # Snare on 3
            (bar_start + 1.125, 42, 100),  # Hihat on 4
            (bar_start + 1.5, 36, 100),  # Kick on 1
            (bar_start + 1.875, 42, 100),  # Hihat on 2
            (bar_start + 2.25, 38, 100),  # Snare on 3
            (bar_start + 2.625, 42, 100),  # Hihat on 4
        ]
    elif bar == 4:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.375, 42, 100),  # Hihat on 2
            (bar_start + 0.75, 38, 100),  # Snare on 3
            (bar_start + 1.125, 42, 100),  # Hihat on 4
            (bar_start + 1.5, 36, 100),  # Kick on 1
            (bar_start + 1.875, 42, 100),  # Hihat on 2
            (bar_start + 2.25, 38, 100),  # Snare on 3
            (bar_start + 2.625, 42, 100),  # Hihat on 4
        ]
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
