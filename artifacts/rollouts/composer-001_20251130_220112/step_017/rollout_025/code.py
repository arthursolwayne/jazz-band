
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
    (36, 0.0, 1.0),       # Kick on beat 1
    (38, 0.5, 1.0),       # Snare on beat 2
    (42, 0.0, 1.0),       # Hihat on beat 1
    (42, 0.25, 0.75),     # Hihat on beat 1 & 2
    (42, 0.5, 1.0),       # Hihat on beat 2
    (42, 0.75, 1.0),      # Hihat on beat 3
    (36, 1.0, 1.5),       # Kick on beat 3
    (38, 1.5, 1.5),       # Snare on beat 4
    (42, 1.0, 1.5),       # Hihat on beat 3 & 4
    (42, 1.25, 1.5),      # Hihat on beat 3 & 4
    (42, 1.5, 1.5),       # Hihat on beat 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    (45, 1.5, 1.5),       # D on beat 1
    (47, 2.0, 2.0),       # F on beat 2
    (48, 2.5, 2.5),       # G on beat 3
    (45, 3.0, 3.0),       # D on beat 4
    (47, 3.5, 3.5),       # F on beat 1
    (48, 4.0, 4.0),       # G on beat 2
    (50, 4.5, 4.5),       # A on beat 3
    (48, 5.0, 5.0),       # G on beat 4
    (47, 5.5, 5.5),       # F on beat 1
    (50, 6.0, 6.0),       # A on beat 2
    (52, 6.5, 6.5),       # Bb on beat 3
    (50, 7.0, 7.0),       # A on beat 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (50, 2.0, 0.5),        # A7 on beat 2
    (52, 2.0, 0.5),        # Bb7 on beat 2
    (53, 2.0, 0.5),        # B7 on beat 2
    (48, 2.0, 0.5),        # G7 on beat 2
    # Bar 3
    (50, 3.5, 0.5),        # A7 on beat 2
    (52, 3.5, 0.5),        # Bb7 on beat 2
    (53, 3.5, 0.5),        # B7 on beat 2
    (48, 3.5, 0.5),        # G7 on beat 2
    # Bar 4
    (50, 5.0, 0.5),        # A7 on beat 2
    (52, 5.0, 0.5),        # Bb7 on beat 2
    (53, 5.0, 0.5),        # B7 on beat 2
    (48, 5.0, 0.5),        # G7 on beat 2
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Dante (Motif)
sax_notes = [
    (62, 1.5, 0.5),        # E on beat 1
    (64, 2.0, 0.5),        # F# on beat 2
    (65, 2.5, 0.5),        # G on beat 3
    (62, 3.0, 0.5),        # E on beat 4
    (64, 3.5, 0.5),        # F# on beat 1
    (66, 4.0, 0.5),        # A on beat 2
    (67, 4.5, 0.5),        # A# on beat 3
    (65, 5.0, 0.5),        # G on beat 4
    (64, 5.5, 0.5),        # F# on beat 1
    (62, 6.0, 0.5),        # E on beat 2
    (60, 6.5, 0.5),        # D on beat 3
    (62, 7.0, 0.5),        # E on beat 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
