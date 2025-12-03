
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

# Bass line: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - Eb - D - E
    (1.5, 38), (1.875, 40), (2.25, 41), (2.625, 42),
    # Bar 3: Bb - A - G - Ab
    (3.0, 37), (3.375, 38), (3.75, 39), (4.125, 40),
    # Bar 4: F - Eb - D - E
    (4.5, 38), (4.875, 40), (5.25, 41), (5.625, 42)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> open voicing
piano_notes = [
    # Bar 2: Fm7
    (1.5, 62), (1.5, 60), (1.5, 55), (1.5, 57),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 57), (3.0, 50), (3.0, 52), (3.0, 55),
    # Bar 4: Fm7 -> Fm9 (F, Ab, C, Eb, G)
    (4.5, 62), (4.5, 60), (4.5, 55), (4.5, 57), (4.5, 65)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 1.5)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (62) -> G (63) -> Eb (60) -> rest
sax_notes = [
    (1.5, 62), (1.75, 63), (2.0, 60), (2.5, 62), (2.75, 63), (3.0, 60)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=115, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
