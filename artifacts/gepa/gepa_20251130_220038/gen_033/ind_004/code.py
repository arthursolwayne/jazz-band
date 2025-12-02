
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray (drums only) - 0.0 to 1.5s
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=hihat, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=hihat, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=hihat, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=hihat, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Walking line in 4/4 (quarter note per beat), chromatic approaches

# Bass notes (quarter note on each beat)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (71)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Gb (69)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Ab (67)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # Bb (65)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # B (64)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Db (62)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Eb (60)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Db (approach to Eb)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Db (chromatic)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # B (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # Bb (resolve)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4

# Fm7 = F, Ab, Bb, Db
# Bars 2-4, comp on beats 2 and 4

# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # Beat 2: Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Db
    # Beat 4: Fm7
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # Db
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # Db
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # Db
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, make it sing. Start it, leave it hanging, come back to finish it.

# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Motif: F (71) -> Ab (67) -> Bb (65) -> B (64)
# Start on beat 2 of bar 2, play the first 3 notes, leave the B hanging, then resolve it on beat 2 of bar 4

sax_notes = [
    # Bar 2 (beat 2) - F, Ab, Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),
    # Bar 4 (beat 2) - resolve to B
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0)
]
sax.notes.extend(sax_notes)

# Bar 2-4: Drums continue (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=kick, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=kick, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 0.375, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=hihat, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=hihat, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=hihat, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=hihat, start=bar_start + 1.125, end=bar_start + 1.5)

    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
