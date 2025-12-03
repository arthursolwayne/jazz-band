
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
    (0.75, 42, 110), # Hihat on & of 1
    (1.125, 38, 100), # Snare on beat 2
    (1.5, 36, 100),  # Kick on beat 3
    (1.75, 42, 110), # Hihat on & of 3
    (2.125, 38, 100), # Snare on beat 4
    (2.5, 42, 110), # Hihat on & of 4
    (3.0, 36, 100)  # Kick on beat 1 of next bar (but we only go to 1.5s)
]
for time, note, velocity in drum_notes:
    if time <= 1.5:
        drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    (1.5, 64, 100), # D2 (root)
    (1.75, 66, 100), # Eb2 (chromatic approach)
    (2.0, 67, 100), # E2 (fifth)
    (2.25, 65, 100), # D#2 (chromatic approach)
    (2.5, 64, 100), # D2 (root)
    (2.75, 66, 100), # Eb2 (chromatic approach)
    (3.0, 67, 100), # E2 (fifth)
    (3.25, 65, 100), # D#2 (chromatic approach)
    (3.5, 64, 100), # D2 (root)
    (3.75, 66, 100), # Eb2 (chromatic approach)
    (4.0, 67, 100), # E2 (fifth)
    (4.25, 65, 100), # D#2 (chromatic approach)
    (4.5, 64, 100), # D2 (root)
    (4.75, 66, 100), # Eb2 (chromatic approach)
    (5.0, 67, 100), # E2 (fifth)
    (5.25, 65, 100), # D#2 (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes_bar2 = [(1.5, 62, 90), (1.5, 64, 90), (1.5, 67, 90), (1.5, 71, 90)]
# Bar 3: Gm7 (G Bb D F)
piano_notes_bar3 = [(2.5, 67, 90), (2.5, 69, 90), (2.5, 71, 90), (2.5, 74, 90)]
# Bar 4: Cm7 (C Eb G Bb)
piano_notes_bar4 = [(3.5, 60, 90), (3.5, 63, 90), (3.5, 67, 90), (3.5, 71, 90)]

for time, note, velocity in piano_notes_bar2:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))
for time, note, velocity in piano_notes_bar3:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))
for time, note, velocity in piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> Eb (63) -> C (60) -> rest. Repeat with variation.
# Motif starts at bar 2, repeats at bar 3 with a slight variation.
sax_notes = [
    (1.5, 62, 100), # D
    (1.75, 63, 100), # Eb
    (2.0, 60, 100), # C
    (2.25, 0, 0),   # Rest
    (2.5, 62, 100), # D
    (2.75, 63, 100), # Eb
    (3.0, 60, 100), # C
    (3.25, 0, 0),   # Rest
    (3.5, 62, 100), # D
    (3.75, 63, 100), # Eb
    (4.0, 60, 100), # C
    (4.25, 0, 0),   # Rest
    (4.5, 62, 100), # D
    (4.75, 63, 100), # Eb
    (5.0, 60, 100), # C
    (5.25, 0, 0),   # Rest
]
for time, note, velocity in sax_notes:
    if note != 0:
        sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))
    else:
        sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: continue in bars 2-4
drum_notes = [
    (1.5, 36, 100), # Kick on beat 1
    (1.75, 42, 110), # Hihat on & of 1
    (2.0, 38, 100), # Snare on beat 2
    (2.25, 42, 110), # Hihat on & of 2
    (2.5, 36, 100), # Kick on beat 3
    (2.75, 42, 110), # Hihat on & of 3
    (3.0, 38, 100), # Snare on beat 4
    (3.25, 42, 110), # Hihat on & of 4
    (3.5, 36, 100), # Kick on beat 1
    (3.75, 42, 110), # Hihat on & of 1
    (4.0, 38, 100), # Snare on beat 2
    (4.25, 42, 110), # Hihat on & of 2
    (4.5, 36, 100), # Kick on beat 3
    (4.75, 42, 110), # Hihat on & of 3
    (5.0, 38, 100), # Snare on beat 4
    (5.25, 42, 110), # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
