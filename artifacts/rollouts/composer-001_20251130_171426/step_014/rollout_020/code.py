
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.625)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.6875)
    # Add notes to drums
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4, hihat5])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif in D, make it sing
# Start with D, then A, then C, then D again — leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.625)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.6875)
    # Add notes to drums
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4, hihat5])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
