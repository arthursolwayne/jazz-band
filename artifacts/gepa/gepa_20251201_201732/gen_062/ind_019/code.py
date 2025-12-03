
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
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on &2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking in D (D2-G2, MIDI 38-43)
bass_notes = [
    (1.5, 43, 100),  # G2 on beat 1
    (2.0, 42, 100),  # F#2 on &1 (chromatic approach)
    (2.5, 38, 100),  # D2 on beat 2
    (3.0, 43, 100),  # G2 on &2
    (3.5, 41, 100),  # E2 on beat 3
    (4.0, 40, 100),  # D#2 on &3 (chromatic approach)
    (4.5, 38, 100),  # D2 on beat 4
    (5.0, 43, 100)   # G2 on &4
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100),  # D
    (1.5, 67, 100),  # F#
    (1.5, 71, 100),  # A
    (1.5, 76, 100),  # C#
    # Bar 3: D7 (D-F#-A-C)
    (3.0, 62, 100),  # D
    (3.0, 67, 100),  # F#
    (3.0, 71, 100),  # A
    (3.0, 74, 100),  # C
    # Bar 4: Dm7 (D-F-A-C)
    (4.5, 62, 100),  # D
    (4.5, 65, 100),  # F
    (4.5, 71, 100),  # A
    (4.5, 76, 100)   # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(100, 36, start + 0.0, start + 0.125))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(100, 38, start + 0.5, start + 0.625))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(100, 36, start + 1.0, start + 1.125))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(100, 38, start + 1.5, start + 1.625))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(100, 42, start + i * 0.125, start + i * 0.125 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (67) - A (71) - D (62) - rest
# Start on beat 2, leave hanging, come back on beat 4
sax_notes = [
    (2.0, 62, 100),  # D on beat 2
    (2.25, 67, 100), # F# on &
    (2.5, 71, 100),  # A on beat 3
    (2.75, 62, 100), # D on &
    (4.0, 62, 100),  # D on beat 4
    (4.25, 67, 100), # F# on &
    (4.5, 71, 100),  # A on beat 5
    (4.75, 62, 100)  # D on &
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
