
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Acoustic piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:  # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:  # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
        # Hi-Hat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# -----------------------------
# Bass: Marcus - walking line in Fm, chromatic approaches
# Fm7 = F, Ab, C, Eb
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),  # F (71)
    pretty_midi.Note(velocity=80, pitch=69, start=1.625, end=1.75),  # Eb (69)
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=1.875),  # E (70)
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),   # D (68)
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.125),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5),   # F
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=70, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=68, start=2.875, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# -----------------------------
# Piano: Diane - 7th chords, comping on 2 & 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# Ab7 = Ab, C, Eb, G

# Bar 2 (On 2 & 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # Ab (64)
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.75),  # C (67)
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),  # F (60)
    pretty_midi.Note(velocity=90, pitch=62, start=1.625, end=1.75),  # Eb (62)

    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),   # F

    # Bar 3 (On 2 & 4)
    pretty_midi.Note(velocity=90, pitch=60, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.125, end=2.25),  # G

    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),   # F

    # Bar 4 (On 2 & 4)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),  # G

    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),   # F
]
piano.notes.extend(piano_notes)

# -----------------------------
# Drums: Little Ray - full on, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Starting from bar 2 (time = 1.5s)
for bar in range(2, 4):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:  # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:  # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
        # Hi-Hat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.125))

# -----------------------------
# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db (but we'll use F, Ab, Bb, C for simplicity)
# Motif: F -> Ab -> Bb -> C (quarter notes), rest on the 4th beat

sax_notes = [
    # Bar 2 (Start the motif)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F (65)
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # Ab (62)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb (60)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # C (67)
    
    # Bar 3 (Rest, then repeat)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # C
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
