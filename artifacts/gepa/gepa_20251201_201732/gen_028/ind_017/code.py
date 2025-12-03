
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time per bar in seconds (160 BPM, 4/4 time)
bar_length = 1.5

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 to 1.5s
drum_notes = [
    (0.0, kick), (0.375, hihat), (0.75, kick), (1.125, hihat),
    (1.5, snare), (1.875, hihat)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Start of the quartet (1.5 - 3.0s)
# Bass: Marcus - walking line (roots and fifths with chromatic approaches)
# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Sax: Dante - one short motif, make it sing, leave it hanging
# Drums: same as before

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    (1.5, 38), (1.875, 39), (2.25, 40), (2.625, 41),  # D2, Eb2, E2, F2
    (3.0, 43), (3.375, 42), (3.75, 41), (4.125, 40)   # G2, F2, E2, D2
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Bar 2: D7 (D F# A C) open voicing
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74),  # D4, F#4, A4, C5
    (1.5, 79), (1.5, 84), (1.5, 87), (1.5, 89),  # D5, F#5, A5, C6
    (1.5, 92)  # D6
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: One short motif, starting at 1.5s
# Motif: D4 - F4 - Eb4 - D4 (sings, then resolves)
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 64), (1.5, 62)  # D4, F4, Eb4, D4
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Bar 3: 3.0 - 4.5s
# Bass: Continue walking
bass_notes = [
    (3.0, 38), (3.375, 39), (3.75, 40), (4.125, 41),  # D2, Eb2, E2, F2
    (4.5, 43), (4.875, 42), (5.25, 41), (5.625, 40)   # G2, F2, E2, D2
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Bar 3: G7 (G B D F) open voicing
piano_notes = [
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76),  # G4, B4, D5, F5
    (3.0, 80), (3.0, 84), (3.0, 87), (3.0, 89),  # G5, B5, D6, F6
    (3.0, 92)  # G6
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums: same as before
# Bar 3: 3.0 - 4.5s
drum_notes = [
    (3.0, kick), (3.375, hihat), (3.75, kick), (4.125, hihat),
    (4.5, snare), (4.875, hihat)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 4: 4.5 - 6.0s
# Bass: Continue walking
bass_notes = [
    (4.5, 38), (4.875, 39), (5.25, 40), (5.625, 41),  # D2, Eb2, E2, F2
    (6.0, 43), (6.375, 42), (6.75, 41), (7.125, 40)   # G2, F2, E2, D2
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Bar 4: C7 (C E G B) open voicing
piano_notes = [
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71),  # C4, E4, G4, B4
    (4.5, 74), (4.5, 77), (4.5, 80), (4.5, 84),  # C5, E5, G5, B5
    (4.5, 87)  # C6
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: Resolve the motif (end of bar 4)
# D4 - Bb4 - C4 - D4 (resolve on D4)
sax_notes = [
    (4.5, 62), (4.5, 67), (4.5, 60), (4.5, 62)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums: same as before
# Bar 4: 4.5 - 6.0s
drum_notes = [
    (4.5, kick), (4.875, hihat), (5.25, kick), (5.625, hihat),
    (6.0, snare), (6.375, hihat)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
# midi.write disabled
