
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.75),    # Hihat on 1&2
    (38, 0.75, 1.125),  # Snare on 2
    (42, 0.75, 1.5),    # Hihat on 2&3
    (36, 1.125, 1.5),   # Kick on 3
    (42, 1.125, 1.5),   # Hihat on 3&4
    (38, 1.5, 1.875),   # Snare on 4
    (42, 1.5, 2.25)     # Hihat on 4&1
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, start, end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (44, 1.5, 1.75),    # F (root)
    (43, 1.75, 2.0),    # Eb (chromatic approach)
    (45, 2.0, 2.25),    # Gb (3rd)
    (46, 2.25, 2.5),    # Ab (4th)
    (44, 2.5, 2.75),    # F (root)
    (43, 2.75, 3.0),    # Eb (chromatic approach)
    (45, 3.0, 3.25),    # Gb (3rd)
    (46, 3.25, 3.5),    # Ab (4th)
    (44, 3.5, 3.75),    # F (root)
    (43, 3.75, 4.0),    # Eb (chromatic approach)
    (45, 4.0, 4.25),    # Gb (3rd)
    (46, 4.25, 4.5),    # Ab (4th)
    (44, 4.5, 4.75),    # F (root)
    (43, 4.75, 5.0),    # Eb (chromatic approach)
    (45, 5.0, 5.25),    # Gb (3rd)
    (46, 5.25, 5.5),    # Ab (4th)
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(70, note, start, end))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.75, 2.0),    # Bb7 (Fm7)
    (53, 1.75, 2.0),
    (57, 1.75, 2.0),
    (60, 1.75, 2.0),
    # Bar 3
    (50, 3.25, 3.5),    # Bb7
    (53, 3.25, 3.5),
    (57, 3.25, 3.5),
    (60, 3.25, 3.5),
    # Bar 4
    (50, 4.75, 5.0),    # Bb7
    (53, 4.75, 5.0),
    (57, 4.75, 5.0),
    (60, 4.75, 5.0),
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(90, note, start, end))

# Dante: Melody in Fm, one short motif, make it sing
sax_notes = [
    (53, 1.5, 1.75),    # Eb (start motif)
    (50, 1.75, 2.0),    # F (end of first phrase)
    (53, 2.0, 2.25),    # Eb (repeat motif)
    (50, 2.25, 2.5),    # F (end of second phrase)
    (57, 2.5, 2.75),    # Ab (extension)
    (50, 2.75, 3.0),    # F (return to motif)
    (53, 3.0, 3.25),    # Eb (motif)
    (50, 3.25, 3.5),    # F (end of third phrase)
    (57, 3.5, 3.75),    # Ab (extension)
    (50, 3.75, 4.0),    # F (return to motif)
    (53, 4.0, 4.25),    # Eb (motif)
    (50, 4.25, 4.5),    # F (end of fourth phrase)
    (57, 4.5, 4.75),    # Ab (extension)
    (50, 4.75, 5.0),    # F (final resolution)
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, start, end))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.875),   # Kick on 1
    (42, 1.5, 2.0),     # Hihat on 1&2
    (38, 2.0, 2.375),   # Snare on 2
    (42, 2.0, 2.5),     # Hihat on 2&3
    (36, 2.375, 2.75),  # Kick on 3
    (42, 2.375, 2.75),  # Hihat on 3&4
    (38, 2.75, 3.125),  # Snare on 4
    (42, 2.75, 3.25),   # Hihat on 4&1
    # Bar 3
    (36, 3.0, 3.375),   # Kick on 1
    (42, 3.0, 3.5),     # Hihat on 1&2
    (38, 3.5, 3.875),   # Snare on 2
    (42, 3.5, 4.0),     # Hihat on 2&3
    (36, 3.875, 4.25),  # Kick on 3
    (42, 3.875, 4.25),  # Hihat on 3&4
    (38, 4.25, 4.625),  # Snare on 4
    (42, 4.25, 4.75),   # Hihat on 4&1
    # Bar 4
    (36, 4.5, 4.875),   # Kick on 1
    (42, 4.5, 5.0),     # Hihat on 1&2
    (38, 5.0, 5.375),   # Snare on 2
    (42, 5.0, 5.5),     # Hihat on 2&3
    (36, 5.375, 5.75),  # Kick on 3
    (42, 5.375, 5.75),  # Hihat on 3&4
    (38, 5.75, 6.125),  # Snare on 4
    (42, 5.75, 6.25)    # Hihat on 4&1
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, start, end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
