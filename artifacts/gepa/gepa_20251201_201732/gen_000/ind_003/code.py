
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
    pretty_midi.Note(start=0.0, end=0.375, pitch=36, velocity=100),  # Kick on 1
    pretty_midi.Note(start=0.0, end=0.375, pitch=42, velocity=80),   # Hihat on 1
    pretty_midi.Note(start=0.375, end=0.75, pitch=42, velocity=80),  # Hihat on 2
    pretty_midi.Note(start=0.75, end=1.125, pitch=36, velocity=100), # Kick on 3
    pretty_midi.Note(start=1.125, end=1.5, pitch=42, velocity=80),   # Hihat on 3
    pretty_midi.Note(start=1.5, end=1.875, pitch=38, velocity=100),  # Snare on 4
    pretty_midi.Note(start=1.5, end=1.875, pitch=42, velocity=80),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(start=1.5, end=1.875, pitch=47, velocity=90),  # F (bar 2, beat 1)
    pretty_midi.Note(start=1.875, end=2.25, pitch=49, velocity=90), # G (bar 2, beat 2)
    pretty_midi.Note(start=2.25, end=2.625, pitch=48, velocity=90), # F# (chromatic)
    pretty_midi.Note(start=2.625, end=3.0, pitch=50, velocity=90),  # A (bar 2, beat 3)

    pretty_midi.Note(start=3.0, end=3.375, pitch=50, velocity=90),  # A (bar 3, beat 1)
    pretty_midi.Note(start=3.375, end=3.75, pitch=52, velocity=90), # B (bar 3, beat 2)
    pretty_midi.Note(start=3.75, end=4.125, pitch=51, velocity=90), # A# (chromatic)
    pretty_midi.Note(start=4.125, end=4.5, pitch=47, velocity=90),  # F (bar 3, beat 3)

    pretty_midi.Note(start=4.5, end=4.875, pitch=47, velocity=90),  # F (bar 4, beat 1)
    pretty_midi.Note(start=4.875, end=5.25, pitch=49, velocity=90), # G (bar 4, beat 2)
    pretty_midi.Note(start=5.25, end=5.625, pitch=48, velocity=90), # F# (chromatic)
    pretty_midi.Note(start=5.625, end=6.0, pitch=50, velocity=90),  # A (bar 4, beat 3)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolving on the last beat of each bar
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(start=1.5, end=1.875, pitch=71, velocity=100),
    pretty_midi.Note(start=1.5, end=1.875, pitch=76, velocity=100),
    pretty_midi.Note(start=1.5, end=1.875, pitch=77, velocity=100),
    pretty_midi.Note(start=1.5, end=1.875, pitch=79, velocity=100),
    
    # Bar 3: Bm7b5 (B, D, F, A)
    pretty_midi.Note(start=3.0, end=3.375, pitch=76, velocity=100),
    pretty_midi.Note(start=3.0, end=3.375, pitch=71, velocity=100),
    pretty_midi.Note(start=3.0, end=3.375, pitch=69, velocity=100),
    pretty_midi.Note(start=3.0, end=3.375, pitch=74, velocity=100),
    
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(start=4.5, end=4.875, pitch=74, velocity=100),
    pretty_midi.Note(start=4.5, end=4.875, pitch=77, velocity=100),
    pretty_midi.Note(start=4.5, end=4.875, pitch=79, velocity=100),
    pretty_midi.Note(start=4.5, end=4.875, pitch=81, velocity=100),
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(start=1.5, end=2.0, pitch=66, velocity=110),  # F (5th)
    pretty_midi.Note(start=2.0, end=2.25, pitch=69, velocity=110),  # A (7th)
    pretty_midi.Note(start=2.25, end=2.5, pitch=65, velocity=110),  # E (3rd)
    
    # Bar 3: Leave it hanging
    pretty_midi.Note(start=3.0, end=3.25, pitch=68, velocity=110),  # G (9th)
    pretty_midi.Note(start=3.25, end=3.5, pitch=67, velocity=110),  # F# (chromatic)
    
    # Bar 4: Finish it
    pretty_midi.Note(start=4.5, end=5.0, pitch=66, velocity=110),  # F (5th)
    pretty_midi.Note(start=5.0, end=5.25, pitch=69, velocity=110),  # A (7th)
    pretty_midi.Note(start=5.25, end=5.5, pitch=65, velocity=110),  # E (3rd)
    pretty_midi.Note(start=5.5, end=6.0, pitch=62, velocity=110),  # C (root)
]
sax.notes.extend(sax_notes)

# Drums: Continue the same pattern for bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    drum_notes = [
        pretty_midi.Note(start=start_time, end=start_time+0.375, pitch=36, velocity=100),  # Kick on 1
        pretty_midi.Note(start=start_time, end=start_time+0.375, pitch=42, velocity=80),   # Hihat on 1
        pretty_midi.Note(start=start_time+0.375, end=start_time+0.75, pitch=42, velocity=80),  # Hihat on 2
        pretty_midi.Note(start=start_time+0.75, end=start_time+1.125, pitch=36, velocity=100), # Kick on 3
        pretty_midi.Note(start=start_time+1.125, end=start_time+1.5, pitch=42, velocity=80),   # Hihat on 3
        pretty_midi.Note(start=start_time+1.5, end=start_time+1.875, pitch=38, velocity=100),  # Snare on 4
        pretty_midi.Note(start=start_time+1.5, end=start_time+1.875, pitch=42, velocity=80),   # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
