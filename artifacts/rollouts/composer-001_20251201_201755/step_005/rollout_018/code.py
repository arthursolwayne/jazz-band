
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36),  # Kick on beat 1
    (0.375, 42), # Hihat
    (0.75, 38),  # Snare on beat 2
    (1.125, 42), # Hihat
    (1.5, 36),   # Kick on beat 3
    (1.875, 42), # Hihat
    (2.25, 38),  # Snare on beat 4
    (2.625, 42)  # Hihat
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking line, roots and fifths with chromatic approaches)
bass_notes = [
    (1.5, 40), (1.75, 41), (2.0, 40), (2.25, 38), # Fm - Bb - F - D
    (2.5, 38), (2.75, 39), (3.0, 38), (3.25, 40), # D - Eb - D - F
    (3.5, 40), (3.75, 41), (4.0, 40), (4.25, 38), # F - Bb - F - D
    (4.5, 38), (4.75, 39), (5.0, 38), (5.25, 40)  # D - Eb - D - F
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 53), (1.5, 60), (1.5, 64), (1.5, 66),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (2.5, 59), (2.5, 62), (2.5, 64), (2.5, 60),
    # Bar 4: Dm7 (D, F, A, C)
    (3.5, 62), (3.5, 64), (3.5, 69), (3.5, 67)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65), Ab (67), C (69), F (65) -> F - Ab - C - F, suspended on the last note
sax_notes = [
    (1.5, 65), (1.5, 67), (1.5, 69), (1.5, 65), # F - Ab - C - F
    (3.0, 65)  # Come back on beat 2 of bar 3
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
