
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.375, 42, 70), # Hihat
    (0.75, 42, 70),  # Hihat
    (1.125, 42, 70), # Hihat
    (1.5, 36, 100),  # Kick on beat 3
    (1.875, 42, 70), # Hihat
    (2.25, 42, 70),  # Hihat
    (2.625, 42, 70), # Hihat
    (3.0, 38, 100),  # Snare on beat 4
    (3.375, 42, 70), # Hihat
    (3.75, 42, 70),  # Hihat
    (4.125, 42, 70), # Hihat
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line with chromatic approach
bass_notes = [
    (1.5, 45, 90),  # F
    (1.875, 46, 90), # F#
    (2.25, 44, 90),  # E
    (2.625, 45, 90), # F
    (3.0, 46, 90),   # F#
    (3.375, 47, 90), # G
    (3.75, 45, 90),  # F
    (4.125, 46, 90), # F#
    (4.5, 48, 90),   # G#
    (4.875, 49, 90), # A
    (5.25, 47, 90),  # G
    (5.625, 46, 90), # F#
    (6.0, 45, 90),   # F
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 44, 80), # E7 (E, G#, B, D)
    (2.25, 50, 80),
    (2.25, 52, 80),
    (2.25, 47, 80),
    # Bar 3
    (3.75, 44, 80), # E7
    (3.75, 50, 80),
    (3.75, 52, 80),
    (3.75, 47, 80),
    # Bar 4
    (5.25, 44, 80), # E7
    (5.25, 50, 80),
    (5.25, 52, 80),
    (5.25, 47, 80),
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Dante: Tenor sax - short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_notes = [
    (1.5, 64, 100), # G
    (1.75, 64, 100), # G
    (2.25, 67, 100), # Bb
    (2.5, 67, 100),  # Bb
    (2.75, 69, 100), # C
    (3.0, 69, 100),  # C
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 3: Leave it hanging
sax_notes = [
    (3.5, 67, 100), # Bb
    (3.75, 67, 100), # Bb
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 4: Come back and finish it
sax_notes = [
    (4.5, 64, 100), # G
    (4.75, 64, 100), # G
    (5.0, 67, 100),  # Bb
    (5.25, 67, 100), # Bb
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
