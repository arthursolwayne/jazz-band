
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
    (36, 0.0, 1.0),     # Kick on 1
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.0, 1.0),     # Hihat on 1
    (42, 0.25, 1.0),    # Hihat on 1+
    (42, 0.5, 1.0),     # Hihat on 2
    (42, 0.75, 1.0),    # Hihat on 2+
    (42, 1.0, 1.0),     # Hihat on 3
    (42, 1.25, 1.0),    # Hihat on 3+
    (42, 1.5, 1.0),     # Hihat on 4
    (36, 1.0, 1.0),     # Kick on 3
    (38, 1.5, 1.0),     # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full ensemble enters
# Sax: short motif, D - F# - B - rests
sax_notes = [
    (62, 1.5, 0.3),     # D
    (66, 1.8, 0.3),     # F#
    (67, 2.1, 0.3),     # B
    (62, 2.4, 0.3),     # D (partial)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: walking line, D - C# - B - A
bass_notes = [
    (62, 1.5, 0.3),     # D
    (61, 1.8, 0.3),     # C#
    (60, 2.1, 0.3),     # B
    (59, 2.4, 0.3),     # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, D7
piano_notes = [
    # D7 on beat 2 (1.8s)
    (62, 1.8, 0.3),     # D
    (67, 1.8, 0.3),     # B
    (64, 1.8, 0.3),     # F#
    (60, 1.8, 0.3),     # A
    # D7 on beat 4 (2.4s)
    (62, 2.4, 0.3),     # D
    (67, 2.4, 0.3),     # B
    (64, 2.4, 0.3),     # F#
    (60, 2.4, 0.3),     # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Drums continue, sax plays partial motif again with space
drum_notes = [
    (36, 1.5, 1.0),     # Kick on 1
    (38, 2.0, 1.0),     # Snare on 2
    (42, 1.5, 1.0),     # Hihat on 1
    (42, 1.75, 1.0),    # Hihat on 1+
    (42, 2.0, 1.0),     # Hihat on 2
    (42, 2.25, 1.0),    # Hihat on 2+
    (42, 2.5, 1.0),     # Hihat on 3
    (42, 2.75, 1.0),    # Hihat on 3+
    (42, 3.0, 1.0),     # Hihat on 4
    (36, 2.5, 1.0),     # Kick on 3
    (38, 3.0, 1.0),     # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: partial motif again, with space
sax_notes = [
    (62, 3.0, 0.3),     # D
    (66, 3.3, 0.3),     # F#
    (67, 3.6, 0.3),     # B
    (62, 3.9, 0.3),     # D (partial)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: walking line, A - G# - G - F#
bass_notes = [
    (59, 3.0, 0.3),     # A
    (58, 3.3, 0.3),     # G#
    (57, 3.6, 0.3),     # G
    (55, 3.9, 0.3),     # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, D7
piano_notes = [
    # D7 on beat 2 (3.3s)
    (62, 3.3, 0.3),     # D
    (67, 3.3, 0.3),     # B
    (64, 3.3, 0.3),     # F#
    (60, 3.3, 0.3),     # A
    # D7 on beat 4 (3.9s)
    (62, 3.9, 0.3),     # D
    (67, 3.9, 0.3),     # B
    (64, 3.9, 0.3),     # F#
    (60, 3.9, 0.3),     # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 4: Drums continue, sax ends with a question, bass resolves, piano holds
drum_notes = [
    (36, 3.0, 1.0),     # Kick on 1
    (38, 3.5, 1.0),     # Snare on 2
    (42, 3.0, 1.0),     # Hihat on 1
    (42, 3.25, 1.0),    # Hihat on 1+
    (42, 3.5, 1.0),     # Hihat on 2
    (42, 3.75, 1.0),    # Hihat on 2+
    (42, 4.0, 1.0),     # Hihat on 3
    (42, 4.25, 1.0),    # Hihat on 3+
    (42, 4.5, 1.0),     # Hihat on 4
    (36, 4.0, 1.0),     # Kick on 3
    (38, 4.5, 1.0),     # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: end motif with a question, D - F# - D (open)
sax_notes = [
    (62, 4.2, 0.3),     # D
    (66, 4.5, 0.3),     # F#
    (62, 4.8, 0.3),     # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: resolves to D
bass_notes = [
    (62, 4.8, 0.3),     # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: D7 on beat 4, hold
piano_notes = [
    (62, 4.5, 0.5),     # D
    (67, 4.5, 0.5),     # B
    (64, 4.5, 0.5),     # F#
    (60, 4.5, 0.5),     # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
