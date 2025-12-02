
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante (tenor sax)
bass = pretty_midi.Instrument(program=33)      # Marcus (bass)
piano = pretty_midi.Instrument(program=0)      # Diane (piano)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray (drums)

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100),# Hihat on &2
    (1.5, 38, 100),  # Snare on 3
    (1.875, 42, 100),# Hihat on &3
    (2.25, 42, 100), # Hihat on &4
    (2.625, 42, 100),# Hihat on &4
    (3.0, 36, 100),  # Kick on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D (root)
    (1.75, 64, 100),  # Eb (chromatic up)
    (2.0, 65, 100),   # E
    (2.25, 67, 100),  # F#
    (2.5, 69, 100),   # G
    (2.75, 71, 100),  # A
    (3.0, 72, 100),   # Bb (chromatic down)
    (3.25, 71, 100),  # A
    (3.5, 69, 100),   # G
    (3.75, 67, 100),  # F#
    (4.0, 65, 100),   # E
    (4.25, 64, 100),  # Eb
    (4.5, 62, 100),   # D
    (4.75, 60, 100),  # C (chromatic down)
    (5.0, 62, 100),   # D
    (5.25, 64, 100),  # Eb
    (5.5, 65, 100),   # E
    (5.75, 67, 100)   # F#
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.75, 72, 100),  # Bb7 (C, E, G, Bb)
    (1.75, 74, 100),  # D
    (1.75, 76, 100),  # F
    (1.75, 71, 100),  # A
    # Bar 3 (2.5 - 3.0s)
    (2.75, 72, 100),  # Bb7
    (2.75, 74, 100),  # D
    (2.75, 76, 100),  # F
    (2.75, 71, 100),  # A
    # Bar 4 (3.5 - 4.0s)
    (3.75, 72, 100),  # Bb7
    (3.75, 74, 100),  # D
    (3.75, 76, 100),  # F
    (3.75, 71, 100),  # A
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Saxophone: short motif, emotionally charged
sax_notes = [
    (1.5, 65, 100),   # E
    (1.75, 67, 100),  # F#
    (2.0, 69, 100),   # G
    (2.25, 65, 100),  # E (rest for 0.25s)
    (2.5, 69, 100),   # G
    (2.75, 71, 100),  # A
    (3.0, 69, 100),   # G
    (3.25, 67, 100),  # F#
    (3.5, 65, 100),   # E
    (3.75, 67, 100),  # F#
    (4.0, 69, 100),   # G
    (4.25, 71, 100),  # A
    (4.5, 69, 100),   # G
    (4.75, 67, 100),  # F#
    (5.0, 65, 100),   # E
    (5.25, 67, 100),  # F#
    (5.5, 69, 100),   # G
    (5.75, 71, 100)   # A (end on A for resolution)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
