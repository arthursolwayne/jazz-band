
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 64, 100),  # F
    (1.75, 65, 100), # F#
    (2.0, 66, 100),  # G
    (2.25, 67, 100), # G#
    (2.5, 68, 100),  # A
    (2.75, 69, 100), # A#
    (3.0, 70, 100),  # Bb
    (3.25, 71, 100), # B
    (3.5, 72, 100),  # C
    (3.75, 71, 100), # B
    (4.0, 70, 100),  # Bb
    (4.25, 69, 100), # A#
    (4.5, 68, 100),  # A
    (4.75, 67, 100), # G#
    (5.0, 66, 100),  # G
    (5.25, 65, 100), # F#
    (5.5, 64, 100),  # F
    (5.75, 63, 100)  # E
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 64, 100),  # F7
    (1.5, 71, 100),
    (1.75, 64, 100), # Comp on 2
    (1.75, 71, 100),
    (2.0, 64, 100),  # F7
    (2.0, 71, 100),
    # Bar 3
    (2.5, 64, 100),  # F7
    (2.5, 71, 100),
    (2.75, 64, 100), # Comp on 2
    (2.75, 71, 100),
    (3.0, 64, 100),  # F7
    (3.0, 71, 100),
    # Bar 4
    (3.5, 64, 100),  # F7
    (3.5, 71, 100),
    (3.75, 64, 100), # Comp on 2
    (3.75, 71, 100),
    (4.0, 64, 100),  # F7
    (4.0, 71, 100),
    (4.25, 64, 100), # Comp on 2
    (4.25, 71, 100),
    (4.5, 64, 100),  # F7
    (4.5, 71, 100),
    (4.75, 64, 100), # Comp on 2
    (4.75, 71, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    if bar == 2:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.25, 42, 100),  # Hihat on &1
            (bar_start + 0.5, 38, 100),  # Snare on 2
            (bar_start + 0.75, 42, 100),  # Hihat on &2
            (bar_start + 1.0, 36, 100),  # Kick on 3
            (bar_start + 1.25, 42, 100),  # Hihat on &3
            (bar_start + 1.5, 38, 100),  # Snare on 4
            (bar_start + 1.75, 42, 100)  # Hihat on &4
        ]
    # Bar 3
    elif bar == 3:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.25, 42, 100),  # Hihat on &1
            (bar_start + 0.5, 38, 100),  # Snare on 2
            (bar_start + 0.75, 42, 100),  # Hihat on &2
            (bar_start + 1.0, 36, 100),  # Kick on 3
            (bar_start + 1.25, 42, 100),  # Hihat on &3
            (bar_start + 1.5, 38, 100),  # Snare on 4
            (bar_start + 1.75, 42, 100)  # Hihat on &4
        ]
    # Bar 4
    elif bar == 4:
        drum_notes = [
            (bar_start, 36, 100),  # Kick on 1
            (bar_start + 0.25, 42, 100),  # Hihat on &1
            (bar_start + 0.5, 38, 100),  # Snare on 2
            (bar_start + 0.75, 42, 100),  # Hihat on &2
            (bar_start + 1.0, 36, 100),  # Kick on 3
            (bar_start + 1.25, 42, 100),  # Hihat on &3
            (bar_start + 1.5, 38, 100),  # Snare on 4
            (bar_start + 1.75, 42, 100)  # Hihat on &4
        ]
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100),  # G
    (1.75, 69, 100),  # Bb
    (2.0, 67, 100),  # A
    (2.25, 64, 100),  # F
    (2.5, 66, 100),  # G
    (2.75, 69, 100),  # Bb
    (3.0, 67, 100),  # A
    (3.25, 64, 100),  # F
    (3.5, 66, 100),  # G
    (3.75, 69, 100),  # Bb
    (4.0, 67, 100),  # A
    (4.25, 64, 100),  # F
    (4.5, 66, 100),  # G
    (4.75, 69, 100),  # Bb
    (5.0, 67, 100),  # A
    (5.25, 64, 100),  # F
    (5.5, 66, 100),  # G
    (5.75, 69, 100),  # Bb
    (6.0, 67, 100),  # A
    (6.25, 64, 100)   # F
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_piece.mid")
