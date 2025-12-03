
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D, F#)
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 40),
    # Bar 3 (A, C#)
    (3.0, 42), (3.375, 44), (3.75, 42), (4.125, 44),
    # Bar 4 (D, F#)
    (4.5, 38), (4.875, 40), (5.25, 38), (5.625, 40)
]

for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    (1.5, 50), (1.5, 53), (1.5, 57), (1.5, 60),
    # Bar 3: Am7 (A, C#, E, G)
    (3.0, 57), (3.0, 60), (3.0, 64), (3.0, 67),
    # Bar 4: D7 (D, F#, A, C)
    (4.5, 50), (4.5, 53), (4.5, 57), (4.5, 60)
]

for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (65), A (67), D (62)
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 62),
    (2.0, 62), (2.25, 65), (2.5, 67), (2.75, 62),
    (3.0, 62), (3.25, 65), (3.5, 67), (3.75, 62)
]

for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
