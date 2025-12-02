
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2: F -> G -> A -> Bb
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # Bb
    # Bar 3: Bb -> C -> D -> Eb
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # Eb
    # Bar 4: Eb -> F -> G -> A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # D
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # G
]
piano.notes.extend(piano_notes)

# Saxophone (Dante)
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=73, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # G
    # Bar 3: Continue
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=75, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.5),  # A
    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.5, end=start_time + 1.875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.875, end=start_time + 2.25)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.25, end=start_time + 2.625)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.625, end=start_time + 3.0)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])

# Write to MIDI file
midi.write("jazz_intro.mid")
