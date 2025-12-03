
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on &3
    (2.125, 42, 100), # Hihat on &4
    (2.5, 36, 100),  # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass - walking line with chromatic approach
bass_notes = [
    (1.5, 62, 80),  # D2 (root)
    (1.75, 64, 80),  # Eb2 (chromatic approach)
    (2.0, 67, 80),  # G2 (fifth)
    (2.25, 65, 80),  # F2 (chromatic approach)
    (2.5, 62, 80),  # D2
    (2.75, 64, 80),  # Eb2
    (3.0, 67, 80),  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano - open voicings, bar 2 = D7sus4
piano_notes = [
    (1.5, 62, 100),  # D2
    (1.5, 67, 100),  # G2
    (1.5, 72, 100),  # C3
    (1.5, 76, 100),  # F3
    (2.0, 64, 100),  # Eb2 (bar 3 = Dm7)
    (2.0, 69, 100),  # Bb2
    (2.0, 72, 100),  # C3
    (2.0, 77, 100),  # F#3
    (2.5, 62, 100),  # D2 (bar 4 = Bb7)
    (2.5, 67, 100),  # G2
    (2.5, 71, 100),  # Bb2
    (2.5, 76, 100),  # F3
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax - motif (bar 2: D, F#, Bb, rest)
sax_notes = [
    (1.5, 62, 100),  # D3
    (1.75, 66, 100),  # F#3
    (2.0, 69, 100),  # Bb3
    (2.25, 62, 100),  # D3 (reprise)
    (2.5, 62, 100),  # D3
    (2.75, 66, 100),  # F#3
    (3.0, 69, 100),  # Bb3
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass - walking line with chromatic approach
bass_notes = [
    (3.0, 62, 80),  # D2
    (3.25, 64, 80),  # Eb2
    (3.5, 67, 80),  # G2
    (3.75, 65, 80),  # F2
    (4.0, 62, 80),  # D2
    (4.25, 64, 80),  # Eb2
    (4.5, 67, 80),  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano - open voicings, bar 3 = Dm7
piano_notes = [
    (3.0, 62, 100),  # D2
    (3.0, 67, 100),  # G2
    (3.0, 71, 100),  # Bb2
    (3.0, 72, 100),  # C3
    (3.5, 64, 100),  # Eb2 (bar 4 = Bb7)
    (3.5, 69, 100),  # Bb2
    (3.5, 72, 100),  # C3
    (3.5, 76, 100),  # F3
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax - motif (bar 3: D, F#, Bb, rest)
sax_notes = [
    (3.0, 62, 100),  # D3
    (3.25, 66, 100),  # F#3
    (3.5, 69, 100),  # Bb3
    (3.75, 62, 100),  # D3 (reprise)
    (4.0, 62, 100),  # D3
    (4.25, 66, 100),  # F#3
    (4.5, 69, 100),  # Bb3
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums - Bar 3
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on &1
    (4.125, 42, 100), # Hihat on &2
    (4.5, 38, 100),  # Snare on beat 2
    (4.75, 42, 100), # Hihat on &3
    (5.125, 42, 100), # Hihat on &4
    (5.5, 36, 100),  # Kick on beat 3
    (6.0, 38, 100),  # Snare on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass - walking line with chromatic approach
bass_notes = [
    (4.5, 62, 80),  # D2
    (4.75, 64, 80),  # Eb2
    (5.0, 67, 80),  # G2
    (5.25, 65, 80),  # F2
    (5.5, 62, 80),  # D2
    (5.75, 64, 80),  # Eb2
    (6.0, 67, 80),  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano - open voicings, bar 4 = Bb7
piano_notes = [
    (4.5, 64, 100),  # Eb2
    (4.5, 69, 100),  # Bb2
    (4.5, 72, 100),  # C3
    (4.5, 76, 100),  # F3
    (5.0, 64, 100),  # Eb2
    (5.0, 69, 100),  # Bb2
    (5.0, 72, 100),  # C3
    (5.0, 76, 100),  # F3
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax - motif (bar 4: D, F#, Bb, rest)
sax_notes = [
    (4.5, 62, 100),  # D3
    (4.75, 66, 100),  # F#3
    (5.0, 69, 100),  # Bb3
    (5.25, 62, 100),  # D3 (reprise)
    (5.5, 62, 100),  # D3
    (5.75, 66, 100),  # F#3
    (6.0, 69, 100),  # Bb3
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums - Bar 4
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (5.25, 42, 100), # Hihat on &3
    (5.5, 38, 100),  # Snare on beat 2
    (5.75, 42, 100), # Hihat on &4
    (6.0, 36, 100),  # Kick on beat 3
    (6.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
