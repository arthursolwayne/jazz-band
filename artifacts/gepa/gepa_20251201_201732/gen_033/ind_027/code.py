
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100), # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 43, 100),  # D2 (root)
    (1.75, 42, 100), # C#2 (chromatic approach)
    (2.0, 38, 100),  # F2 (fifth)
    (2.25, 39, 100), # G2 (root)
    (2.5, 43, 100),  # F2 (fifth)
    (2.75, 42, 100), # E2 (chromatic approach)
    (3.0, 38, 100),  # D2 (root)
    (3.25, 39, 100), # D2 (root)
    (3.5, 43, 100),  # F2 (fifth)
    (3.75, 42, 100), # E2 (chromatic approach)
    (4.0, 38, 100),  # C2 (chromatic approach)
    (4.25, 39, 100), # D2 (root)
    (4.5, 43, 100),  # F2 (fifth)
    (4.75, 42, 100), # E2 (chromatic approach)
    (5.0, 38, 100),  # D2 (root)
    (5.25, 39, 100), # D2 (root)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    (1.5, 57, 100),  # F (Dm7)
    (1.5, 60, 100),  # A
    (1.5, 62, 100),  # D
    (1.5, 64, 100),  # F
    # Bar 3: G7 (B, D, G, B)
    (2.5, 62, 100),  # B
    (2.5, 65, 100),  # D
    (2.5, 67, 100),  # G
    (2.5, 69, 100),  # B
    # Bar 4: Cm7 (E, G, C, E)
    (3.5, 64, 100),  # E
    (3.5, 67, 100),  # G
    (3.5, 72, 100),  # C
    (3.5, 76, 100),  # E
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on & of 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100), # Hihat on & of 2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on & of 4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100), # Hihat on & of 2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on & of 3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100), # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (F, A, D) with a chromatic run to C
sax_notes = [
    (1.5, 62, 100),  # D4 (D)
    (1.6, 64, 100),  # E4 (chromatic)
    (1.7, 60, 100),  # C4 (resolve down)
    (2.0, 62, 100),  # D4 (return)
    (2.1, 64, 100),  # E4 (chromatic)
    (2.2, 60, 100),  # C4 (resolve down)
    (2.5, 62, 100),  # D4 (return)
    (2.6, 64, 100),  # E4 (chromatic)
    (2.7, 60, 100),  # C4 (resolve down)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
