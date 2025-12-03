
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 38), (1.875, 40), (2.25, 42), (2.625, 43),
    # Bar 3
    (3.0, 43), (3.375, 41), (3.75, 38), (4.125, 40),
    # Bar 4
    (4.5, 40), (4.875, 38), (5.25, 42), (5.625, 43)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 69),
    # Bar 3: Gm7 (G, Bb, D, F)
    (3.0, 67), (3.0, 70), (3.0, 72), (3.0, 74),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (4.5, 60), (4.5, 63), (4.5, 67), (4.5, 70)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (Dm scale: D, E, F, G)
    (1.5, 62), (1.625, 64), (1.75, 65), (1.875, 67),
    # Bar 3: Leave it hanging, then come back
    (3.0, 67), (3.125, 65), (3.25, 64), (3.375, 62),
    # Bar 4: Finish the motif, resolve
    (4.5, 62), (4.625, 64), (4.75, 65), (4.875, 67)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
