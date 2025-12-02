
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
    (36, 0.0),      # Kick on 1
    (42, 0.375),    # Hihat
    (38, 0.75),     # Snare on 2
    (42, 1.125),    # Hihat
    (36, 1.5),      # Kick on 3
    (42, 1.875),    # Hihat
    (38, 2.25),     # Snare on 4
    (42, 2.625)     # Hihat
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: All instruments join
# Bass: Walking line in D minor, chromatic approaches
# Dm7: D F A C
bass_notes = [
    (62, 1.5),      # D
    (63, 1.875),    # Eb (chromatic)
    (62, 2.25),     # D
    (60, 2.625),    # B (chromatic)
]
for note, time in bass_notes:
    nb = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
piano_notes = [
    (62, 2.25),     # D
    (67, 2.25),     # A
    (64, 2.25),     # F
    (69, 2.25),     # C
    (62, 2.625),    # D
    (67, 2.625),    # A
    (64, 2.625),    # F
    (69, 2.625),    # C
]
for note, time in piano_notes:
    np = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(np)

# Sax: One short motif, make it sing. Start it, leave it hanging.
# D - F# - Bb (half note on 1, 8th on 2, 8th on 3, rest on 4)
sax_notes = [
    (62, 1.5),      # D
    (66, 1.875),    # F#
    (64, 2.25),     # Bb
]
for note, time in sax_notes:
    ns = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(ns)

# Bar 3: All instruments
# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    (62, 3.0),      # D
    (63, 3.375),    # Eb (chromatic)
    (62, 3.75),     # D
    (60, 4.125),    # B (chromatic)
]
for note, time in bass_notes:
    nb = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.75),     # D
    (67, 3.75),     # A
    (64, 3.75),     # F
    (69, 3.75),     # C
    (62, 4.125),    # D
    (67, 4.125),    # A
    (64, 4.125),    # F
    (69, 4.125),    # C
]
for note, time in piano_notes:
    np = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(np)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0),      # Kick on 1
    (42, 3.375),    # Hihat
    (38, 3.75),     # Snare on 2
    (42, 4.125),    # Hihat
    (36, 4.5),      # Kick on 3
    (42, 4.875),    # Hihat
    (38, 5.25),     # Snare on 4
    (42, 5.625)     # Hihat
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Sax: Second phrase, variation of the motif but ending on a rest
sax_notes = [
    (62, 3.0),      # D
    (66, 3.375),    # F#
    (64, 3.75),     # Bb
]
for note, time in sax_notes:
    ns = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(ns)

# Bar 4: All instruments
# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    (62, 4.5),      # D
    (63, 4.875),    # Eb (chromatic)
    (62, 5.25),     # D
    (60, 5.625),    # B (chromatic)
]
for note, time in bass_notes:
    nb = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 5.25),     # D
    (67, 5.25),     # A
    (64, 5.25),     # F
    (69, 5.25),     # C
    (62, 5.625),    # D
    (67, 5.625),    # A
    (64, 5.625),    # F
    (69, 5.625),    # C
]
for note, time in piano_notes:
    np = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(np)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5),      # Kick on 1
    (42, 4.875),    # Hihat
    (38, 5.25),     # Snare on 2
    (42, 5.625),    # Hihat
    (36, 6.0),      # Kick on 3
    (42, 6.375),    # Hihat
    (38, 6.75),     # Snare on 4
    (42, 7.125)     # Hihat
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Sax: Third phrase, ends with a rest, a question
sax_notes = [
    (62, 4.5),      # D
    (66, 4.875),    # F#
    (64, 5.25),     # Bb
]
for note, time in sax_notes:
    ns = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(ns)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
