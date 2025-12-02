
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),    # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=2.9375),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=2.9375, end=3.125), # B
    pretty_midi.Note(velocity=90, pitch=55, start=3.125, end=3.3125), # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.3125, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.6875),   # A#
    pretty_midi.Note(velocity=90, pitch=52, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.875, end=4.0625), # G#
    pretty_midi.Note(velocity=90, pitch=50, start=4.0625, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.4375),  # F#
    pretty_midi.Note(velocity=90, pitch=48, start=4.4375, end=4.625), # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.625, end=4.8125), # E
    pretty_midi.Note(velocity=90, pitch=46, start=4.8125, end=5.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.1875),   # D
    pretty_midi.Note(velocity=90, pitch=44, start=5.1875, end=5.375), # Db
    pretty_midi.Note(velocity=90, pitch=43, start=5.375, end=5.5625), # C
    pretty_midi.Note(velocity=90, pitch=42, start=5.5625, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=5.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=5.9375, end=6.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7 on beat 2
piano_notes = [
    # Fm7 on beat 2 (bar 2)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),  # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.875, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=2.875, end=3.0),  # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=3.875, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Key is Fm. Motif: F Eb G D
sax_notes = [
    # Bar 2: F Eb G D
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.0),   # G
    # Bar 3: Leave it hanging (no note)
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=51, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=110, pitch=55, start=3.5625, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=3.9375),  # D
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
