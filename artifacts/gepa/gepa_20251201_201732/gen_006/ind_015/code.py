
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
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2 (root)
    (1.75, 40, 100), # Eb2 (chromatic approach)
    (2.0, 43, 100),  # G2 (fifth)
    (2.25, 42, 100), # F2 (chromatic approach)
    (2.5, 38, 100),  # D2 (root)
    (2.75, 40, 100), # Eb2 (chromatic approach)
    (3.0, 43, 100),  # G2 (fifth)
    (3.25, 42, 100), # F2 (chromatic approach)
    (3.5, 38, 100),  # D2 (root)
    (3.75, 40, 100), # Eb2 (chromatic approach)
    (4.0, 43, 100),  # G2 (fifth)
    (4.25, 42, 100), # F2 (chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    (1.5, 62, 100), # D4
    (1.5, 67, 100), # F#4
    (1.5, 71, 100), # A4
    (1.5, 72, 100), # Bb4 (chromatic approach)
    (2.0, 72, 100), # Bb4 (resolve)
]
# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    (2.5, 67, 100), # G4
    (2.5, 71, 100), # B4
    (2.5, 62, 100), # D4
    (2.5, 67, 100), # F#4
    (3.0, 67, 100), # F#4 (resolve)
])
# Bar 4: C#7 (C#, E#, G#, B#)
piano_notes.extend([
    (3.5, 64, 100), # C#4
    (3.5, 69, 100), # E#4 (F4)
    (3.5, 73, 100), # G#4
    (3.5, 76, 100), # B#4 (C4)
    (4.0, 76, 100), # C4 (resolve)
])
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F#4, Bb4, D4 (half note, half note, quarter note, eighth note)
sax_notes = [
    (1.5, 62, 100), # D4 (half note)
    (1.5, 67, 100), # F#4 (half note)
    (2.5, 71, 100), # Bb4 (quarter note)
    (3.0, 62, 100), # D4 (eighth note)
    (3.5, 62, 100), # D4 (half note)
    (3.5, 67, 100), # F#4 (half note)
    (4.5, 71, 100), # Bb4 (quarter note)
    (5.0, 62, 100)  # D4 (eighth note)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drum_notes.append((bar_start + 0.0, 36, 100))
    # Hihat on &1
    drum_notes.append((bar_start + 0.25, 42, 100))
    # Snare on 2
    drum_notes.append((bar_start + 0.5, 38, 100))
    # Hihat on &2
    drum_notes.append((bar_start + 0.75, 42, 100))
    # Kick on 3
    drum_notes.append((bar_start + 1.0, 36, 100))
    # Hihat on &3
    drum_notes.append((bar_start + 1.25, 42, 100))
    # Snare on 4
    drum_notes.append((bar_start + 1.5, 38, 100))
    # Hihat on &4
    drum_notes.append((bar_start + 1.75, 42, 100))

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
