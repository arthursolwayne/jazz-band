
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.125, 0.25), # Hihat on &1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.5, 0.25),   # Hihat on &2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.875, 0.25), # Hihat on &3
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.25, 0.25)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus (walking line, chromatic approaches)
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375)  # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 1.5, 0.125),  # C7: C, E, B
    (64, 1.5, 0.125),
    (67, 1.5, 0.125),
    (60, 2.25, 0.125),
    (64, 2.25, 0.125),
    (67, 2.25, 0.125),
    (60, 3.0, 0.125),
    (64, 3.0, 0.125),
    (67, 3.0, 0.125),
    (60, 3.75, 0.125),
    (64, 3.75, 0.125),
    (67, 3.75, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums - Bars 2-4
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.625, 0.25), # Hihat on &1
    (38, 1.875, 0.375),# Snare on 2
    (42, 2.0, 0.25),   # Hihat on &2
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.375, 0.25), # Hihat on &3
    (38, 2.625, 0.375),# Snare on 4
    (42, 2.75, 0.25),  # Hihat on &4
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.125, 0.25), # Hihat on &1
    (38, 3.375, 0.375),# Snare on 2
    (42, 3.5, 0.25),   # Hihat on &2
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.875, 0.25), # Hihat on &3
    (38, 4.125, 0.375),# Snare on 4
    (42, 4.25, 0.25),  # Hihat on &4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.625, 0.25), # Hihat on &1
    (38, 4.875, 0.375),# Snare on 2
    (42, 5.0, 0.25),   # Hihat on &2
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.375, 0.25), # Hihat on &3
    (38, 5.625, 0.375),# Snare on 4
    (42, 5.75, 0.25)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Dante (melody in bars 2-4, one short motif, make it sing)
sax_notes = [
    (62, 1.5, 0.5),    # D (bar 2, beat 1)
    (64, 2.0, 0.5),    # E (bar 2, beat 2)
    (62, 2.5, 0.5),    # D (bar 2, beat 3)
    (60, 3.0, 0.5),    # C (bar 2, beat 4)
    (62, 3.5, 0.5),    # D (bar 3, beat 1)
    (64, 4.0, 0.5),    # E (bar 3, beat 2)
    (62, 4.5, 0.5),    # D (bar 3, beat 3)
    (60, 5.0, 0.5),    # C (bar 3, beat 4)
    (62, 5.5, 0.5)     # D (bar 4, beat 1 - leave it hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
