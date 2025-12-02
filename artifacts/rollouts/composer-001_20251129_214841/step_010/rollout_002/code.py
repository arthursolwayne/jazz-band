
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
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875), # Hihat on 1& 
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.75, 0.1875), # Hihat on 3&
    (42, 1.125, 0.1875), # Hihat on 4&
    (36, 1.5, 0.375)  # Kick on beat 3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in C, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C on beat 1
    (61, 1.875, 0.375), # C# on beat 2
    (62, 2.25, 0.375),  # D on beat 3
    (63, 2.625, 0.375), # D# on beat 4
    (63, 3.0, 0.375),  # D# on beat 1
    (64, 3.375, 0.375), # E on beat 2
    (65, 3.75, 0.375),  # F on beat 3
    (66, 4.125, 0.375), # F# on beat 4
    (67, 4.5, 0.375),   # G on beat 1
    (68, 4.875, 0.375), # G# on beat 2
    (69, 5.25, 0.375),  # A on beat 3
    (70, 5.625, 0.375)  # A# on beat 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.1875), # C7: C, E, B
    (64, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    (64, 2.625, 0.1875), # C7
    (60, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    # Bar 3
    (60, 3.375, 0.1875), # C7
    (64, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (64, 4.125, 0.1875), # C7
    (60, 4.125, 0.1875),
    (69, 4.125, 0.1875),
    # Bar 4
    (60, 4.875, 0.1875), # C7
    (64, 4.875, 0.1875),
    (69, 4.875, 0.1875),
    (64, 5.625, 0.1875), # C7
    (60, 5.625, 0.1875),
    (69, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on beat 1
    (38, 1.875, 0.375), # Snare on beat 2
    (42, 1.5, 0.1875), # Hihat on 1&
    (42, 1.875, 0.1875), # Hihat on 2&
    (42, 2.25, 0.1875), # Hihat on 3&
    (42, 2.625, 0.1875), # Hihat on 4&
    (36, 2.25, 0.375),  # Kick on beat 3
    (38, 2.625, 0.375), # Snare on beat 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on beat 1
    (38, 3.375, 0.375), # Snare on beat 2
    (42, 3.0, 0.1875), # Hihat on 1&
    (42, 3.375, 0.1875), # Hihat on 2&
    (42, 3.75, 0.1875), # Hihat on 3&
    (42, 4.125, 0.1875), # Hihat on 4&
    (36, 3.75, 0.375),  # Kick on beat 3
    (38, 4.125, 0.375), # Snare on beat 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on beat 1
    (38, 4.875, 0.375), # Snare on beat 2
    (42, 4.5, 0.1875), # Hihat on 1&
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.25, 0.1875), # Hihat on 3&
    (42, 5.625, 0.1875), # Hihat on 4&
    (36, 5.25, 0.375),  # Kick on beat 3
    (38, 5.625, 0.375), # Snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone - short motif, make it sing
sax_notes = [
    (62, 1.5, 0.5),    # D on beat 1
    (65, 2.0, 0.5),    # F on beat 2
    (67, 2.5, 0.5),    # G on beat 3
    (65, 3.0, 0.5),    # F on beat 4
    (62, 3.5, 0.5),    # D on beat 1
    (64, 4.0, 0.5),    # E on beat 2
    (67, 4.5, 0.5),    # G on beat 3
    (69, 5.0, 0.5),    # A on beat 4
    (67, 5.5, 0.5),    # G on beat 1
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo.mid')
