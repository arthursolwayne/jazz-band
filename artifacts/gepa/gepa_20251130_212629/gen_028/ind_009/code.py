
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
    (36, 1.0, 0.5, 100),    # Kick on 1
    (42, 1.0, 0.25, 80),    # Hihat on 2
    (38, 1.0, 0.25, 100),   # Snare on 2
    (42, 1.375, 0.25, 80),  # Hihat on 3
    (36, 1.5, 0.5, 100),    # Kick on 3
    (42, 1.75, 0.25, 80),   # Hihat on 4
    (38, 1.75, 0.25, 100),  # Snare on 4
]
for note, start, duration, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.25, 80),    # D
    (63, 1.75, 0.25, 80),   # Eb (chromatic)
    (62, 2.0, 0.25, 80),    # D
    (60, 2.25, 0.25, 80),   # B (chromatic)
    (62, 2.5, 0.25, 80),    # D
    (64, 2.75, 0.25, 80),   # F (chromatic)
    (62, 3.0, 0.25, 80),    # D
    (61, 3.25, 0.25, 80),   # C# (chromatic)
    (62, 3.5, 0.25, 80),    # D
    (63, 3.75, 0.25, 80),   # Eb (chromatic)
    (62, 4.0, 0.25, 80),    # D
    (60, 4.25, 0.25, 80),   # B (chromatic)
    (62, 4.5, 0.25, 80),    # D
    (64, 4.75, 0.25, 80),   # F (chromatic)
    (62, 5.0, 0.25, 80),    # D
    (61, 5.25, 0.25, 80),   # C# (chromatic)
]
for note, start, duration, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 2.0, 0.25, 80),     # D7: D
    (67, 2.0, 0.25, 80),     # D7: A
    (64, 2.0, 0.25, 80),     # D7: F
    (69, 2.0, 0.25, 80),     # D7: C
    # Bar 3
    (62, 3.5, 0.25, 80),     # D7: D
    (67, 3.5, 0.25, 80),     # D7: A
    (64, 3.5, 0.25, 80),     # D7: F
    (69, 3.5, 0.25, 80),     # D7: C
    # Bar 4
    (62, 5.0, 0.25, 80),     # D7: D
    (67, 5.0, 0.25, 80),     # D7: A
    (64, 5.0, 0.25, 80),     # D7: F
    (69, 5.0, 0.25, 80),     # D7: C
]
for note, start, duration, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (66), D (62), rest
sax_notes = [
    (62, 1.75, 0.25, 100),   # Start on 2
    (66, 2.0, 0.25, 100),    # F#
    (62, 2.25, 0.25, 100),   # D
    (62, 2.75, 0.25, 100),   # Repeat D on 3
    (66, 3.0, 0.25, 100),    # F#
    (62, 3.25, 0.25, 100),   # D
    (62, 3.75, 0.25, 100),   # Repeat D on 4
]
for note, start, duration, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + duration))

# Drums: Continue in bars 2-4
drum_notes = [
    # Bar 2
    (36, 2.0, 0.5, 100),     # Kick on 1
    (42, 2.0, 0.25, 80),     # Hihat on 2
    (38, 2.0, 0.25, 100),    # Snare on 2
    (42, 2.375, 0.25, 80),   # Hihat on 3
    (36, 2.5, 0.5, 100),     # Kick on 3
    (42, 2.75, 0.25, 80),    # Hihat on 4
    (38, 2.75, 0.25, 100),   # Snare on 4
    # Bar 3
    (36, 3.5, 0.5, 100),     # Kick on 1
    (42, 3.5, 0.25, 80),     # Hihat on 2
    (38, 3.5, 0.25, 100),    # Snare on 2
    (42, 3.875, 0.25, 80),   # Hihat on 3
    (36, 4.0, 0.5, 100),     # Kick on 3
    (42, 4.25, 0.25, 80),    # Hihat on 4
    (38, 4.25, 0.25, 100),   # Snare on 4
    # Bar 4
    (36, 4.5, 0.5, 100),     # Kick on 1
    (42, 4.5, 0.25, 80),     # Hihat on 2
    (38, 4.5, 0.25, 100),    # Snare on 2
    (42, 4.875, 0.25, 80),   # Hihat on 3
    (36, 5.0, 0.5, 100),     # Kick on 3
    (42, 5.25, 0.25, 80),    # Hihat on 4
    (38, 5.25, 0.25, 100),   # Snare on 4
]
for note, start, duration, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
