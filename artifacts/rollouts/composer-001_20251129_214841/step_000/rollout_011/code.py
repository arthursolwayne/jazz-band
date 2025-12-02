
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.0, 1.0),     # Hihat on 1
    (36, 0.75, 1.0),    # Kick on 3
    (42, 0.75, 1.0),    # Hihat on 3
    (38, 1.0, 1.0),     # Snare on 2
    (42, 1.0, 1.0),     # Hihat on 2
    (38, 1.5, 1.0),     # Snare on 4
    (42, 1.5, 1.0)      # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (60, 1.5, 0.5),    # C
    (61, 2.0, 0.5),    # C#
    (62, 2.5, 0.5),    # D
    (63, 3.0, 0.5),    # D#
    (64, 3.5, 0.5),    # E
    (65, 4.0, 0.5),    # F
    (66, 4.5, 0.5),    # F#
    (67, 5.0, 0.5),    # G
    (68, 5.5, 0.5),    # G#
    (69, 6.0, 0.5)     # A
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (64, 2.0, 0.5),    # C7
    (69, 2.0, 0.5),
    (71, 2.0, 0.5),
    (72, 2.0, 0.5),
    # Bar 3
    (64, 3.0, 0.5),    # C7
    (69, 3.0, 0.5),
    (71, 3.0, 0.5),
    (72, 3.0, 0.5),
    # Bar 4
    (64, 4.0, 0.5),    # C7
    (69, 4.0, 0.5),
    (71, 4.0, 0.5),
    (72, 4.0, 0.5)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.0),    # Kick on 1
    (42, 1.5, 1.0),    # Hihat on 1
    (36, 2.25, 1.0),   # Kick on 3
    (42, 2.25, 1.0),   # Hihat on 3
    (38, 2.5, 1.0),    # Snare on 2
    (42, 2.5, 1.0),    # Hihat on 2
    (38, 3.0, 1.0),    # Snare on 4
    (42, 3.0, 1.0),    # Hihat on 4
    # Bar 3
    (36, 3.5, 1.0),    # Kick on 1
    (42, 3.5, 1.0),    # Hihat on 1
    (36, 4.25, 1.0),   # Kick on 3
    (42, 4.25, 1.0),   # Hihat on 3
    (38, 4.5, 1.0),    # Snare on 2
    (42, 4.5, 1.0),    # Hihat on 2
    (38, 5.0, 1.0),    # Snare on 4
    (42, 5.0, 1.0),    # Hihat on 4
    # Bar 4
    (36, 5.5, 1.0),    # Kick on 1
    (42, 5.5, 1.0),    # Hihat on 1
    (36, 6.25, 1.0),   # Kick on 3
    (42, 6.25, 1.0),   # Hihat on 3
    (38, 6.5, 1.0),    # Snare on 2
    (42, 6.5, 1.0),    # Hihat on 2
    (38, 7.0, 1.0),    # Snare on 4
    (42, 7.0, 1.0)     # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: Dante (melody in bars 2-4)
sax_notes = [
    # Bar 2
    (62, 2.0, 0.5),    # D
    (66, 2.5, 0.5),    # F#
    (67, 3.0, 0.5),    # G
    (69, 3.5, 0.5),    # A
    # Bar 3
    (67, 4.0, 0.5),    # G
    (69, 4.5, 0.5),    # A
    (66, 5.0, 0.5),    # F#
    (62, 5.5, 0.5),    # D
    # Bar 4
    (64, 6.0, 0.5),    # E
    (66, 6.5, 0.5),    # F#
    (67, 7.0, 0.5),    # G
    (69, 7.5, 0.5)     # A
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
