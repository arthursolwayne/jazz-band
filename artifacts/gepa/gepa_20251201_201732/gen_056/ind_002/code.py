
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36, 100), # Kick on 1
    (0.375, 42, 110), # Hihat
    (0.75, 42, 110),
    (1.125, 42, 110),
    (1.5, 38, 100), # Snare on 2
    (1.875, 42, 110),
    (2.25, 42, 110),
    (2.625, 42, 110),
    (3.0, 36, 100), # Kick on 3
    (3.375, 42, 110),
    (3.75, 42, 110),
    (4.125, 42, 110),
    (4.5, 38, 100), # Snare on 4
    (4.875, 42, 110),
    (5.25, 42, 110),
    (5.625, 42, 110)
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (Bass): Walking line in Dm, roots and fifths with chromatic approaches
# D2 - F2 - D2 - C#2 (bar 2)
# F2 - A2 - F2 - E2 (bar 3)
# D2 - F2 - D2 - C#2 (bar 4)

bass_notes = [
    # Bar 2
    (1.5, 38, 100), # D2
    (1.875, 43, 100), # F2
    (2.25, 38, 100), # D2
    (2.625, 41, 100), # C#2
    # Bar 3
    (3.0, 43, 100), # F2
    (3.375, 47, 100), # A2
    (3.75, 43, 100), # F2
    (4.125, 46, 100), # E2
    # Bar 4
    (4.5, 38, 100), # D2
    (4.875, 43, 100), # F2
    (5.25, 38, 100), # D2
    (5.625, 41, 100) # C#2
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F - A - C - D)
# Bar 3: Gm7 (G - B - D - E)
# Bar 4: Dm7 (D - F - A - C)

piano_notes = [
    # Bar 2
    (1.5, 41, 100), # F
    (1.5, 46, 100), # A
    (1.5, 52, 100), # C
    (1.5, 55, 100), # D
    # Bar 3
    (3.0, 47, 100), # G
    (3.0, 53, 100), # B
    (3.0, 58, 100), # D
    (3.0, 61, 100), # E
    # Bar 4
    (4.5, 50, 100), # D
    (4.5, 55, 100), # F
    (4.5, 62, 100), # A
    (4.5, 64, 100)  # C
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.5))

# Dante (Sax): Tenor Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, Eb4, D4 (first bar)
# Then rests, then repeat and finish on C4

sax_notes = [
    # Bar 2
    (1.5, 62, 110), # D4
    (1.625, 67, 110), # F4
    (1.75, 65, 110), # Eb4
    (1.875, 62, 110), # D4
    # Bar 3 - Rest
    # Bar 4
    (4.5, 62, 110), # D4
    (4.625, 67, 110), # F4
    (4.75, 65, 110), # Eb4
    (4.875, 60, 110) # C4
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
