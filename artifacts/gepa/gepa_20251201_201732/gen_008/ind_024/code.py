
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
    (0.0, 36, 100),    # kick on 1
    (0.75, 42, 100),   # hihat on &1
    (1.0, 38, 100),    # snare on 2
    (1.25, 42, 100),   # hihat on &2
    (1.5, 36, 100),    # kick on 3
    (1.75, 42, 100),   # hihat on &3
    (2.0, 38, 100),    # snare on 4
    (2.25, 42, 100),   # hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 43, 100),    # G2
    (1.75, 41, 100),   # E2
    (2.0, 43, 100),    # G2
    (2.25, 40, 100),   # D2
    # Bar 3 (3.0 - 4.5s)
    (3.0, 40, 100),    # D2
    (3.25, 42, 100),   # F2
    (3.5, 40, 100),    # D2
    (3.75, 39, 100),   # C2
    # Bar 4 (4.5 - 6.0s)
    (4.5, 39, 100),    # C2
    (4.75, 41, 100),   # E2
    (5.0, 39, 100),    # C2
    (5.25, 38, 100),   # B1
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 53, 100),    # F (MIDI 53)
    (1.5, 60, 100),    # Ab (MIDI 60)
    (1.5, 65, 100),    # C (MIDI 65)
    (1.5, 67, 100),    # D (MIDI 67)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 58, 100),    # Bb
    (3.0, 62, 100),    # D
    (3.0, 53, 100),    # F
    (3.0, 60, 100),    # Ab
    # Bar 4: Am7 (A, C, E, G)
    (4.5, 57, 100),    # A
    (4.5, 60, 100),    # C
    (4.5, 64, 100),    # E
    (4.5, 67, 100),    # G
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36, 100),    # kick on 1
    (1.75, 42, 100),   # hihat on &1
    (2.0, 38, 100),    # snare on 2
    (2.25, 42, 100),   # hihat on &2
    (2.5, 36, 100),    # kick on 3
    (2.75, 42, 100),   # hihat on &3
    (3.0, 38, 100),    # snare on 4
    (3.25, 42, 100),   # hihat on &4
    # Bar 3 (3.0 - 4.5s)
    (3.0, 36, 100),    # kick on 1
    (3.25, 42, 100),   # hihat on &1
    (3.5, 38, 100),    # snare on 2
    (3.75, 42, 100),   # hihat on &2
    (4.0, 36, 100),    # kick on 3
    (4.25, 42, 100),   # hihat on &3
    (4.5, 38, 100),    # snare on 4
    (4.75, 42, 100),   # hihat on &4
    # Bar 4 (4.5 - 6.0s)
    (4.5, 36, 100),    # kick on 1
    (4.75, 42, 100),   # hihat on &1
    (5.0, 38, 100),    # snare on 2
    (5.25, 42, 100),   # hihat on &2
    (5.5, 36, 100),    # kick on 3
    (5.75, 42, 100),   # hihat on &3
    (6.0, 38, 100),    # snare on 4
    (6.25, 42, 100),   # hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F (53) - Ab (60) - Bb (62) - C (65)
# Play on beats 1 and 3 of bar 2, then 2 and 4 of bar 3, then 1 and 3 of bar 4

sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 53, 100),    # F on 1
    (2.0, 60, 100),    # Ab on 3
    # Bar 3 (3.0 - 4.5s)
    (3.25, 62, 100),   # Bb on &2
    (3.75, 65, 100),   # C on &4
    # Bar 4 (4.5 - 6.0s)
    (4.5, 53, 100),    # F on 1
    (5.0, 60, 100),    # Ab on 3
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
