
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
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 38, 100), (1.125, 42, 100),
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100),
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 43, 90),   # F (root)
    (1.875, 40, 90), # Ab (chromatic approach)
    (2.25, 38, 90),  # D (fifth)
    (2.625, 41, 90), # Bb (chromatic approach)
    (3.0, 43, 90),   # F (root)
    (3.375, 40, 90), # Ab (chromatic approach)
    (3.75, 38, 90),  # D (fifth)
    (4.125, 41, 90), # Bb (chromatic approach)
    (4.5, 43, 90),   # F (root)
    (4.875, 40, 90), # Ab (chromatic approach)
    (5.25, 38, 90),  # D (fifth)
    (5.625, 41, 90), # Bb (chromatic approach)
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    # Bar 2
    (1.5, 53, 100), (1.5, 60, 100), (1.5, 64, 100), (1.5, 67, 100),  # Fm7
    # Bar 3
    (2.25, 59, 100), (2.25, 62, 100), (2.25, 65, 100), (2.25, 68, 100),  # Bb7
    # Bar 4
    (3.0, 57, 100), (3.0, 60, 100), (3.0, 65, 100), (3.0, 67, 100),  # E7
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - D - rest (0.75s), then F - Eb - F (0.75s)
sax_notes = [
    (1.5, 64, 100), (1.5 + 0.375, 62, 100), (1.5 + 0.75, 60, 100),
    (1.5 + 1.125, 64, 100), (1.5 + 1.5, 62, 100), (1.5 + 1.875, 64, 100),
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: continue for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    for start, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity, note, start + 1.5 + i * 3.0, start + 1.5 + i * 3.0 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
