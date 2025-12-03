
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 40),
    (3.0, 40), (3.375, 42), (3.75, 40), (4.125, 42),
    (4.5, 42), (4.875, 44), (5.25, 42), (5.625, 44)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G) - open voicing
    (1.5, 62), (1.5, 67), (1.5, 70), (1.5, 74),
    # Bar 3: Bbm7 (D, F, Ab, Bb) - open voicing
    (3.0, 65), (3.0, 67), (3.0, 70), (3.0, 71),
    # Bar 4: Gm7 (Bb, D, F, G) - open voicing
    (4.5, 62), (4.5, 67), (4.5, 70), (4.5, 74)
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (70) - F (72) - Ab (74) - D (70) (half note, then rest, then D (70))
sax_notes = [
    (1.5, 70), (1.5, 72), (1.5, 74), (1.5, 70),
    (3.0, 70)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.75)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
