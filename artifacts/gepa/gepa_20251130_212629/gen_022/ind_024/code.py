
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.875, 0.125),  # Hihat
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.25, 0.125)    # Hihat
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.25),  # D (root)
    (63, 1.75, 0.25),  # Eb (chromatic approach)
    (60, 2.0, 0.25),  # Bb (3rd)
    (62, 2.25, 0.25)  # D (root)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.0, 0.25),  # D7 (D, F#, A, C)
    (67, 2.0, 0.25),
    (69, 2.0, 0.25),
    (64, 2.0, 0.25),
    (64, 2.25, 0.25),
    (67, 2.25, 0.25),
    (69, 2.25, 0.25),
    (62, 2.25, 0.25)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.125),  # Hihat
    (38, 1.75, 0.375),  # Snare on 2
    (42, 1.75, 0.125),  # Hihat
    (36, 2.0, 0.375),  # Kick on 3
    (42, 2.0, 0.125),  # Hihat
    (38, 2.25, 0.375),  # Snare on 4
    (42, 2.25, 0.125)   # Hihat
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: One short motif, make it sing. Start, leave it hanging, come back and finish
sax_notes = [
    (65, 2.0, 0.25),  # E (first note of motif)
    (67, 2.5, 0.25),  # G (second note)
    (65, 3.0, 0.25),  # E (third note)
    (62, 3.5, 0.25)   # D (resolve)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (64, 3.0, 0.25),  # F (7th)
    (62, 3.25, 0.25),  # D (root)
    (65, 3.5, 0.25),  # E (chromatic)
    (64, 3.75, 0.25)  # F (7th)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.0, 0.25),  # D7
    (67, 3.0, 0.25),
    (69, 3.0, 0.25),
    (64, 3.0, 0.25),
    (64, 3.25, 0.25),
    (67, 3.25, 0.25),
    (69, 3.25, 0.25),
    (62, 3.25, 0.25)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat
    (38, 3.25, 0.375),  # Snare on 2
    (42, 3.25, 0.125),  # Hihat
    (36, 3.5, 0.375),  # Kick on 3
    (42, 3.5, 0.125),  # Hihat
    (38, 3.75, 0.375),  # Snare on 4
    (42, 3.75, 0.125)   # Hihat
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: Continue motif with variation
sax_notes = [
    (62, 3.0, 0.25),  # D (first note of motif)
    (64, 3.5, 0.25),  # F (second note)
    (62, 4.0, 0.25),  # D (third note)
    (60, 4.5, 0.25)   # Bb (resolve)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (60, 4.5, 0.25),  # Bb (3rd)
    (62, 4.75, 0.25),  # D (root)
    (63, 5.0, 0.25),  # Eb (chromatic)
    (60, 5.25, 0.25)  # Bb (3rd)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.5, 0.25),  # D7
    (67, 4.5, 0.25),
    (69, 4.5, 0.25),
    (64, 4.5, 0.25),
    (64, 4.75, 0.25),
    (67, 4.75, 0.25),
    (69, 4.75, 0.25),
    (62, 4.75, 0.25)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat
    (38, 4.75, 0.375),  # Snare on 2
    (42, 4.75, 0.125),  # Hihat
    (36, 5.0, 0.375),  # Kick on 3
    (42, 5.0, 0.125),  # Hihat
    (38, 5.25, 0.375),  # Snare on 4
    (42, 5.25, 0.125)   # Hihat
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: End motif with a question, not a statement
sax_notes = [
    (60, 4.5, 0.25),  # Bb (first note of motif)
    (62, 5.0, 0.25),  # D (second note)
    (60, 5.5, 0.25),  # Bb (third note)
    (64, 6.0, 0.25)   # F (question)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
