
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

# Drums - Bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # 1st bar
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # 2nd bar
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # 3rd bar
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # 4th bar
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Bar 2: Walking line with chromatic approaches
# D2 (D2 = MIDI 38)
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 38), (2.25, 41),  # Bar 2
    (2.5, 43), (2.75, 41), (3.0, 38), (3.25, 40),  # Bar 3
    (3.5, 38), (3.75, 40), (4.0, 38), (4.25, 41),  # Bar 4
    (4.5, 43), (4.75, 41), (5.0, 38), (5.25, 40)   # Bar 5 (part of 4th bar)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano - Bar 2: Open voicings, different chord each bar
# Bar 2: G7 (G B D F) - D2, F3, B3, G4
# Bar 3: A7 (A C# E G) - C#2, E3, A4, G4
# Bar 4: F7 (F A C E) - F2, A3, C4, E4

piano_notes_bar2 = [(1.5, 67), (1.5, 69), (1.5, 76), (1.5, 71)]
piano_notes_bar3 = [(2.5, 60), (2.5, 64), (2.5, 76), (2.5, 71)]
piano_notes_bar4 = [(3.5, 65), (3.5, 69), (3.5, 67), (3.5, 74)]

for time, note in piano_notes_bar2:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=2.0)
    piano.notes.append(piano_note)

for time, note in piano_notes_bar3:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=3.0)
    piano.notes.append(piano_note)

for time, note in piano_notes_bar4:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=4.0)
    piano.notes.append(piano_note)

# Saxophone - Bar 2: Melody, one short motif, make it sing
# Start on D4 (MIDI 62), syncopated rhythm, leave it hanging

sax_notes = [
    (1.75, 62), (2.25, 64), (2.75, 62), (3.25, 64)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
