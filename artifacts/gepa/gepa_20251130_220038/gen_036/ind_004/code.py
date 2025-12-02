
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
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on &2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (1.5, 42, 100),  # Fm7: F, Ab, C, D
    (1.75, 40, 100), # Bb
    (2.0, 43, 100),  # C
    (2.25, 41, 100), # D
    (2.5, 42, 100),  # F
    (2.75, 40, 100), # Bb
    (3.0, 43, 100),  # C
    (3.25, 41, 100), # D
    (3.5, 42, 100),  # F
    (3.75, 40, 100), # Bb
    (4.0, 43, 100),  # C
    (4.25, 44, 100), # Eb
    (4.5, 42, 100),  # F
    (4.75, 40, 100), # Bb
    (5.0, 43, 100),  # C
    (5.25, 41, 100)  # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.25))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 62, 100), (1.75, 60, 100), (1.75, 63, 100), (1.75, 64, 100),  # Dm7
    (2.25, 62, 100), (2.25, 60, 100), (2.25, 63, 100), (2.25, 64, 100),  # Dm7
    (3.75, 62, 100), (3.75, 60, 100), (3.75, 63, 100), (3.75, 64, 100),  # Dm7
    (4.25, 62, 100), (4.25, 60, 100), (4.25, 63, 100), (4.25, 64, 100)   # Dm7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.25))

# Drums (Little Ray) - full kit
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100)  # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Saxophone (Dante) - one short motif, make it sing
sax_notes = [
    (1.5, 64, 100),  # F
    (1.75, 62, 100), # D
    (2.0, 65, 100),  # G
    (2.25, 62, 100), # D
    (2.5, 64, 100),  # F
    (2.75, 61, 100), # C
    (3.0, 66, 100),  # A
    (3.25, 62, 100), # D
    (3.5, 64, 100),  # F
    (3.75, 61, 100), # C
    (4.0, 66, 100),  # A
    (4.25, 67, 100), # Bb
    (4.5, 64, 100),  # F
    (4.75, 62, 100), # D
    (5.0, 65, 100),  # G
    (5.25, 62, 100)  # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
