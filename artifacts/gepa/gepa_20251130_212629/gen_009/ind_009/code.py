
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes[0].nominator = 4
midi.time_signature_changes[0].denominator = 4

# Set the key signature to D major
midi.key_signature_changes[0].key_number = 2  # D major

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI object
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)
midi.instruments.append(sax)

# Time per bar at 160 BPM: 60 / 160 * 4 = 1.5 seconds
# Time per beat: 0.375 seconds

# Time for 4 bars: 6 seconds
# Time per bar: 1.5 seconds

# Drums - Bar 1: Snare on 2 and 4, hihat on every eighth
def create_drums_bar_1():
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375)
    # Hihat on every 8th
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125)
    hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875)
    hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625)
    hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375)
    hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125)

    # Add all notes to the drum instrument
    drums.notes.extend([kick, kick2, snare, snare2, 
                        hihat, hihat2, hihat3, hihat4, 
                        hihat5, hihat6, hihat7, hihat8, 
                        hihat9, hihat10, hihat11, hihat12])

# Bass - Bar 1: Walking line, chromatic approach
def create_bass_bar_1():
    # Root: D (2nd octave, 62)
    # Chromatic approach to B (66)
    # Then root again, then chromatic approach to F# (69)
    # Keep moving, never the same note
    root = 62
    next_note = 63  # chromatic up
    next_note2 = 66  # B
    next_note3 = 65  # chromatic down to F#
    next_note4 = 69  # F#
    next_note5 = 70  # chromatic up
    next_note6 = 67  # G
    next_note7 = 66  # chromatic down

    notes = [
        pretty_midi.Note(velocity=100, pitch=root, start=0.0, end=0.375),
        pretty_midi.Note(velocity=100, pitch=next_note, start=0.375, end=0.75),
        pretty_midi.Note(velocity=100, pitch=next_note2, start=0.75, end=1.125),
        pretty_midi.Note(velocity=100, pitch=next_note3, start=1.125, end=1.5),
        pretty_midi.Note(velocity=100, pitch=next_note4, start=1.5, end=1.875),
        pretty_midi.Note(velocity=100, pitch=next_note5, start=1.875, end=2.25),
        pretty_midi.Note(velocity=100, pitch=next_note6, start=2.25, end=2.625),
        pretty_midi.Note(velocity=100, pitch=next_note7, start=2.625, end=3.0),
    ]
    bass.notes.extend(notes)

# Piano - Bar 1: Comp on 2 and 4, 7th chords
def create_piano_bar_1():
    # D7 chord at beat 2: D, F#, A, C
    # D7 chord at beat 4: D, F#, A, C
    # Use 7ths, sparse, let the rhythm breathe

    # Beat 2
    d7 = [50, 53, 57, 60]  # D7
    # Beat 4
    d7_4 = [50, 53, 57, 60]

    # Assign start times
    start_2 = 0.75
    start_4 = 2.25

    for pitch in d7:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_2, end=start_2 + 0.1875)
        piano.notes.append(note)
    for pitch in d7_4:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_4, end=start_4 + 0.1875)
        piano.notes.append(note)

# Sax - Bar 1: No sax in first bar, only intro
# Bar 2-4: Start the melody, leave it hanging

def create_sax_bar_2():
    # D minor motif: Dm7 -> G7 -> Cmaj7 -> F7 -> B7 -> E7 -> A7 -> D7
    # Start with a short motif, leave it hanging

    # D (62) -> F# (65) -> A (69) -> C (60)
    # 8th notes
    note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
    note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25)
    note3 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625)
    note4 = pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0)

    sax.notes.extend([note1, note2, note3, note4])

def create_sax_bar_3():
    # G7 -> Cmaj7 -> F7 -> B7
    # D minor scale: D, E, F#, G, A, B, C
    # G7: G, B, D, F
    # Cmaj7: C, E, G, B

    note1 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375)
    note2 = pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75)
    note3 = pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125)
    note4 = pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5)

    sax.notes.extend([note1, note2, note3, note4])

def create_sax_bar_4():
    # E7 -> A7 -> D7
    # E7: E, G#, B, D
    # A7: A, C#, E, G

    note1 = pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875)
    note2 = pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25)
    note3 = pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625)
    note4 = pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0)

    sax.notes.extend([note1, note2, note3, note4])

# Bass - Bar 2-4: Walking line, chromatic approaches
def create_bass_bar_2_4():
    # D, B, F#, G, A, D, C, B
    # Keep moving, chromatic and walking
    notes = [
        pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
        pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),
        pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
        pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
        pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
        pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
        pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
        pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),
        pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
        pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
        pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
        pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),
    ]
    bass.notes.extend(notes)

# Piano - Bar 2-4: Comp on 2 and 4, 7th chords
def create_piano_bar_2_4():
    # Chord progression: Dm7 -> G7 -> Cmaj7 -> F7 -> B7 -> E7 -> A7 -> D7

    # Dm7: D, F, A, C
    # G7: G, B, D, F
    # Cmaj7: C, E, G, B
    # F7: F, A, C, E
    # B7: B, D, F#, A
    # E7: E, G#, B, D
    # A7: A, C#, E, G
    # D7: D, F#, A, C

    chords = [
        (50, 53, 57, 60),  # Dm7
        (67, 69, 62, 65),  # G7
        (60, 64, 67, 69),  # Cmaj7
        (55, 58, 60, 64),  # F7
        (62, 64, 67, 69),  # B7 (approximated)
        (64, 67, 69, 62),  # E7
        (69, 71, 64, 67),  # A7
        (50, 65, 57, 60),  # D7
    ]

    time = 1.5
    for bar in range(2, 6):
        for i in range(len(chords)):
            chord = chords[i]
            start = time + (i * 1.5)
            for pitch in chord:
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.1875)
                piano.notes.append(note)

# Drums - Bars 2-4: Same pattern, just repeating the same 4-bar rhythm
def create_drums_bar_2_4():
    # Repeat the same pattern with offset
    for i in range(2, 6):
        # Kick on 1 and 3
        kick1 = pretty_midi.Note(velocity=100, pitch=36, start=i * 1.5, end=i * 1.5 + 0.375)
        kick2 = pretty_midi.Note(velocity=100, pitch=36, start=i * 1.5 + 1.125, end=i * 1.5 + 1.5)
        # Snare on 2 and 4
        snare1 = pretty_midi.Note(velocity=100, pitch=38, start=i * 1.5 + 0.75, end=i * 1.5 + 0.875)
        snare2 = pretty_midi.Note(velocity=100, pitch=38, start=i * 1.5 + 2.25, end=i * 1.5 + 2.375)
        # Hihat on every 8th
        for j in range(0, 8):
            hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + (j * 0.375), end=i * 1.5 + (j * 0.375) + 0.1875)
            drums.notes.append(hihat)
        # Add kick and snare
        drums.notes.extend([kick1, kick2, snare1, snare2])

# Generate the MIDI
create_drums_bar_1()
create_bass_bar_1()
create_piano_bar_1()

create_sax_bar_2()
create_sax_bar_3()
create_sax_bar_4()

create_bass_bar_2_4()
create_piano_bar_2_4()
create_drums_bar_2_4()

# Write to file
midi.write("dante_intro.mid")
