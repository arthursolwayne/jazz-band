
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
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 64, 100), # F3
    (2.0, 65, 100), # G3
    (2.5, 66, 100), # Ab3
    (3.0, 67, 100), # Bb3
    (3.5, 68, 100), # B3
    (4.0, 69, 100), # C4
    (4.5, 70, 100), # Db4
    (5.0, 71, 100), # D4
    (5.5, 69, 100), # C4
]
for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane - Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 64, 100), # F7 (F, A, C, Eb)
    (2.0, 69, 100),
    (2.0, 71, 100),
    (2.0, 67, 100),
    # Bar 3
    (3.5, 64, 100), # F7
    (3.5, 69, 100),
    (3.5, 71, 100),
    (3.5, 67, 100),
    # Bar 4
    (5.0, 64, 100), # F7
    (5.0, 69, 100),
    (5.0, 71, 100),
    (5.0, 67, 100)
]
for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray - Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on & of 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100), # Hihat on & of 2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on & of 4
    (3.5, 36, 100),  # Kick on beat 1 (bar 3)
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100), # Hihat on & of 2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on & of 3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100), # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante - Sax: Motif (start at bar 2)
# Motif: F - Bb - C - Eb (F7 arpeggio), then leave it hanging on Bb
sax_notes = [
    (2.0, 84, 100),  # F5
    (2.25, 87, 100), # Bb5
    (2.5, 88, 100),  # C6
    (2.75, 85, 100), # Eb5
    (3.0, 87, 100),  # Bb5 (hold)
    (3.0, 87, 100),  # Bb5 (hold)
    (3.0, 87, 100),  # Bb5 (hold)
    (3.0, 87, 100),  # Bb5 (hold)
    (3.5, 84, 100),  # F5 (return)
    (3.75, 87, 100), # Bb5
    (4.0, 88, 100),  # C6
    (4.25, 85, 100), # Eb5
    (4.5, 87, 100),  # Bb5 (hold)
    (4.5, 87, 100),  # Bb5 (hold)
    (4.5, 87, 100),  # Bb5 (hold)
    (4.5, 87, 100),  # Bb5 (hold)
    (5.0, 84, 100),  # F5 (return)
    (5.25, 87, 100), # Bb5
    (5.5, 88, 100),  # C6
    (5.75, 85, 100), # Eb5
    (6.0, 87, 100),  # Bb5 (hold)
    (6.0, 87, 100),  # Bb5 (hold)
    (6.0, 87, 100),  # Bb5 (hold)
    (6.0, 87, 100)   # Bb5 (hold)
]
for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
