
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
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 43, 100), # F2 (root)
    (1.75, 42, 100), # E2 (chromatic approach)
    (2.0, 40, 100), # D2 (fifth)
    (2.25, 43, 100), # F2 (root)
    (2.5, 44, 100), # G2 (fifth)
    (2.75, 42, 100), # E2 (chromatic approach)
    (3.0, 40, 100), # D2 (fifth)
    (3.25, 43, 100), # F2 (root)
    (3.5, 44, 100), # G2 (fifth)
    (3.75, 42, 100), # E2 (chromatic approach)
    (4.0, 40, 100), # D2 (fifth)
    (4.25, 43, 100), # F2 (root)
    (4.5, 44, 100), # G2 (fifth)
    (4.75, 42, 100), # E2 (chromatic approach)
    (5.0, 40, 100), # D2 (fifth)
    (5.25, 43, 100), # F2 (root)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 53, 100), # F (MIDI 53)
    (1.5, 60, 100), # A (MIDI 60)
    (1.5, 64, 100), # C (MIDI 64)
    (1.5, 67, 100), # E (MIDI 67)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    (2.5, 55, 100), # G (MIDI 55)
    (2.5, 59, 100), # Bb (MIDI 59)
    (2.5, 62, 100), # D (MIDI 62)
    (2.5, 64, 100), # F (MIDI 64)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (3.5, 60, 100), # C (MIDI 60)
    (3.5, 64, 100), # E (MIDI 64)
    (3.5, 67, 100), # G (MIDI 67)
    (3.5, 69, 100), # Bb (MIDI 69)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bars 2-4
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, bar_start, bar_start + 0.125))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(100, 42, bar_start + 0.75, bar_start + 0.875))
    # Snare on 3
    drums.notes.append(pretty_midi.Note(100, 38, bar_start + 1.125, bar_start + 1.25))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(100, 42, bar_start + 1.5, bar_start + 1.625))

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (MIDI 53), G# (MIDI 56), E (MIDI 63)
sax_notes = [
    (1.5, 53, 100), # F
    (1.75, 56, 100), # G#
    (2.0, 63, 100), # E
    (2.25, 53, 100), # F
    (2.5, 56, 100), # G#
    (2.75, 63, 100), # E
    (3.0, 53, 100), # F
    (3.25, 56, 100), # G#
    (3.5, 63, 100), # E
    (3.75, 53, 100), # F
    (4.0, 56, 100), # G#
    (4.25, 63, 100), # E
    (4.5, 53, 100), # F
    (4.75, 56, 100), # G#
    (5.0, 63, 100), # E
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
