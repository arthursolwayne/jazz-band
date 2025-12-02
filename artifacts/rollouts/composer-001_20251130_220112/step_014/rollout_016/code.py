
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2: Dm7 - F, Eb, D, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5), # Eb
    # Bar 3: Dm7 - C, Bb, B, C
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75), # C
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.25), # B
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5), # C
    # Bar 4: Dm7 - C, D, Eb, D
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5), # D
    # Bar 5: Dm7 - D, C, Bb, C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0), # C
    pretty_midi.Note(velocity=90, pitch=58, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5), # C
    # Bar 6: Dm7 - C, Bb, B, C
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75), # C
    pretty_midi.Note(velocity=90, pitch=58, start=5.75, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=6.0, end=6.25), # B
    pretty_midi.Note(velocity=90, pitch=60, start=6.25, end=6.5), # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25), # Eb
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75), # Eb
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25), # G
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25), # Eb
    # Bar 5: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75), # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75), # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75), # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75), # Eb
    # Bar 6: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.25), # G
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.25), # C
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.25), # Eb
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax - one short motif, make it sing
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
    # Bar 3: Development
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    # Bar 5: Embellishment
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Eb
    # Bar 6: Final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=6.25, end=6.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-6
for bar in range(2, 6):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)

drums.notes.extend([note for note in drums.notes if note.start < 6.0])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
