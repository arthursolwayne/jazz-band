
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.5, 36, 100),  # Kick on 3
    (2.25, 42, 100), # Hihat on &3
    (2.5, 38, 100),  # Snare on 4
    (3.0, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (1.5, 45, 100),  # F
    (1.75, 46, 100), # F#
    (2.0, 44, 100),  # E
    (2.25, 45, 100), # F
    (2.5, 47, 100),  # G
    (2.75, 49, 100), # A
    (3.0, 47, 100),  # G
    (3.25, 45, 100), # F
    (3.5, 46, 100),  # F#
    (3.75, 44, 100), # E
    (4.0, 45, 100),  # F
    (4.25, 47, 100), # G
    (4.5, 50, 100),  # Bb
    (4.75, 49, 100), # A
    (5.0, 47, 100),  # G
    (5.25, 45, 100), # F
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (2.0, 45, 100),  # F7: F, A, C, Eb
    (2.0, 50, 100),
    (2.0, 52, 100),
    (2.0, 48, 100),
    (2.5, 45, 100),  # F7 again
    (2.5, 50, 100),
    (2.5, 52, 100),
    (2.5, 48, 100),
    (3.0, 45, 100),  # F7 again
    (3.0, 50, 100),
    (3.0, 52, 100),
    (3.0, 48, 100),
    (3.5, 45, 100),  # F7 again
    (3.5, 50, 100),
    (3.5, 52, 100),
    (3.5, 48, 100),
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Saxophone (Dante) - Melody: whisper at first, then build
sax_notes = [
    (1.5, 60, 80),  # F
    (1.75, 64, 75),  # A
    (2.0, 62, 70),  # G
    (2.25, 64, 75),  # A
    (2.5, 65, 80),  # Bb
    (2.75, 67, 85),  # C
    (3.0, 65, 80),  # Bb
    (3.25, 64, 75),  # A
    (3.5, 62, 70),  # G
    (3.75, 64, 75),  # A
    (4.0, 65, 80),  # Bb
    (4.25, 67, 85),  # C
    (4.5, 69, 90),  # D
    (4.75, 67, 85),  # C
    (5.0, 65, 80),  # Bb
    (5.25, 64, 75),  # A
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
