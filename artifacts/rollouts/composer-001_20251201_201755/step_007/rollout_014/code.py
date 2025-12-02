
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
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on &1
    (1.0, 38, 100),   # Snare on 2
    (1.25, 42, 100),  # Hihat on &2
    (1.5, 36, 100),   # Kick on 3
    (1.75, 42, 100),  # Hihat on &3
    (2.0, 38, 100),   # Snare on 4
    (2.25, 42, 100),  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 50, 80),   # D2 (root)
    (1.75, 51, 80),  # Eb2 (chromatic approach)
    (2.0, 52, 80),   # E2 (fifth of G)
    (2.25, 50, 80),  # D2 (root)
    (2.5, 51, 80),   # Eb2 (chromatic approach)
    (2.75, 52, 80),  # E2 (fifth of G)
    (3.0, 50, 80),   # D2 (root)
    (3.25, 51, 80),  # Eb2 (chromatic approach)
    (3.5, 52, 80),   # E2 (fifth of G)
    (3.75, 50, 80),  # D2 (root)
    (4.0, 51, 80),   # Eb2 (chromatic approach)
    (4.25, 52, 80),  # E2 (fifth of G)
    (4.5, 50, 80),   # D2 (root)
    (4.75, 51, 80),  # Eb2 (chromatic approach)
    (5.0, 52, 80),   # E2 (fifth of G)
    (5.25, 50, 80),  # D2 (root)
    (5.5, 51, 80),   # Eb2 (chromatic approach)
    (5.75, 52, 80),  # E2 (fifth of G)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62, 100),  # D4
    (1.5, 65, 100),  # F4
    (1.5, 69, 100),  # A4
    (1.5, 67, 100),  # C4
    # Bar 3: G7 (G, B, D, F)
    (2.5, 67, 100),  # G4
    (2.5, 71, 100),  # B4
    (2.5, 69, 100),  # D4
    (2.5, 65, 100),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.5, 60, 100),  # C4
    (3.5, 63, 100),  # Eb4
    (3.5, 67, 100),  # G4
    (3.5, 62, 100),  # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# You: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 64, 100),  # E4 (start of motif)
    (1.75, 62, 100), # D4
    (2.0, 64, 100),  # E4
    (2.25, 65, 100), # F4 (leave it hanging)
    (3.0, 62, 100),  # D4 (come back)
    (3.25, 64, 100), # E4
    (3.5, 65, 100),  # F4
    (3.75, 62, 100), # D4
    (4.0, 60, 100),  # C4 (resolve)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: continue from bar 2
drum_notes = [
    (1.5, 36, 100),   # Kick on 1
    (1.75, 42, 100),  # Hihat on &1
    (2.0, 38, 100),   # Snare on 2
    (2.25, 42, 100),  # Hihat on &2
    (2.5, 36, 100),   # Kick on 3
    (2.75, 42, 100),  # Hihat on &3
    (3.0, 38, 100),   # Snare on 4
    (3.25, 42, 100),  # Hihat on &4
    (3.5, 36, 100),   # Kick on 1
    (3.75, 42, 100),  # Hihat on &1
    (4.0, 38, 100),   # Snare on 2
    (4.25, 42, 100),  # Hihat on &2
    (4.5, 36, 100),   # Kick on 3
    (4.75, 42, 100),  # Hihat on &3
    (5.0, 38, 100),   # Snare on 4
    (5.25, 42, 100),  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar_intro.mid")
