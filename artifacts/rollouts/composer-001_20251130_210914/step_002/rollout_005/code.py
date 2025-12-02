
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1& 
    (42, 0.1875, 0.1875), # Hihat on 2&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2& 
    (42, 0.5625, 0.1875), # Hihat on 3&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3& 
    (42, 0.9375, 0.1875), # Hihat on 4&
    (38, 1.125, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (48, 1.5, 0.375),  # F
    (49, 1.875, 0.375), # Gb
    (50, 2.25, 0.375),  # G
    (48, 2.625, 0.375), # F
    # Bar 3
    (51, 2.625, 0.375),  # Ab
    (52, 3.0, 0.375),    # Bb
    (51, 3.375, 0.375),  # Ab
    (50, 3.75, 0.375),   # G
    # Bar 4
    (48, 3.75, 0.375),   # F
    (49, 4.125, 0.375),  # Gb
    (50, 4.5, 0.375),    # G
    (48, 4.875, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.1875), # Bb7: Bb
    (53, 1.875, 0.1875), # D
    (57, 1.875, 0.1875), # F
    (60, 1.875, 0.1875), # Ab
    (50, 2.25, 0.1875),  # Bb
    (53, 2.25, 0.1875),  # D
    (57, 2.25, 0.1875),  # F
    (60, 2.25, 0.1875),  # Ab
    # Bar 3
    (50, 3.0, 0.1875),   # Bb
    (53, 3.0, 0.1875),   # D
    (57, 3.0, 0.1875),   # F
    (60, 3.0, 0.1875),   # Ab
    (50, 3.375, 0.1875), # Bb
    (53, 3.375, 0.1875), # D
    (57, 3.375, 0.1875), # F
    (60, 3.375, 0.1875), # Ab
    # Bar 4
    (50, 4.125, 0.1875), # Bb
    (53, 4.125, 0.1875), # D
    (57, 4.125, 0.1875), # F
    (60, 4.125, 0.1875), # Ab
    (50, 4.5, 0.1875),   # Bb
    (53, 4.5, 0.1875),   # D
    (57, 4.5, 0.1875),   # F
    (60, 4.5, 0.1875),   # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # G
    (64, 1.875, 0.375), # A
    (62, 2.25, 0.375),  # G
    (60, 2.625, 0.375), # F
    (62, 3.0, 0.375),   # G
    (64, 3.375, 0.375), # A
    (62, 3.75, 0.375),  # G
    (60, 4.125, 0.375), # F
    (62, 4.5, 0.375),   # G
    (64, 4.875, 0.375), # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
