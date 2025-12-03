
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define the note lengths
note_length = 0.375  # 60 BPM = 1 beat per second, 160 BPM = 0.375s per beat

# Bar 1: Drums only (1.5 seconds)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(bpm, bar_start, instrument):
    beat = 60.0 / bpm
    bar = 4 * beat
    for i in range(4):
        time = bar_start + i * beat
        # Kick on 1 and 3 (0 and 2 beats)
        if i in [0, 2]:
            instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + beat/2))
        # Snare on 2 and 4 (1 and 3 beats)
        if i in [1, 3]:
            instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + beat/2))
        # Hi-hat on every eighth (0, 0.5, 1, 1.5, etc)
        for j in range(2):
            instrument.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time + j * beat/2, end=time + j * beat/2 + beat/4))

add_drums(160, 0.0, drums)

# Bar 2: Bass, Piano, Sax
# Bar start: 1.5 seconds
bar_start = 1.5

# Bass Line (D2 to G2, walking line with chromatic approaches)
bass_notes = [
    (62, 0.0),  # D2
    (64, 0.375),  # E2
    (62, 0.75),  # D2
    (60, 1.125),  # C2 (chromatic approach)
    (62, 1.5),  # D2
    (64, 1.875),  # E2
    (62, 2.25),  # D2
    (60, 2.625),  # C2
    (62, 3.0),  # D2
    (64, 3.375),  # E2
    (62, 3.75),  # D2
    (60, 4.125),  # C2
    (62, 4.5),  # D2
    (64, 4.875),  # E2
    (62, 5.25),  # D2
    (60, 5.625),  # C2
    (62, 6.0)  # D2 (end of bar)
]

for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar_start + start, end=bar_start + start + note_length))

# Piano Chords (Dm, Gm7, Am7, Dm)
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Am7 (A, C, E, G)
# Bar 5: Dm7 (D, F, A, C) — resolve on last bar

def add_piano_chord(chord, start_time):
    if chord == "Dm7":
        notes = [62, 64, 67, 69]  # D, F, A, C
    elif chord == "Gm7":
        notes = [67, 69, 71, 64]  # G, Bb, D, F
    elif chord == "Am7":
        notes = [69, 71, 74, 67]  # A, C, E, G
    else:
        return

    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start_time, end=start_time + note_length))

add_piano_chord("Dm7", bar_start)
add_piano_chord("Gm7", bar_start + 1.5)
add_piano_chord("Am7", bar_start + 3.0)
add_piano_chord("Dm7", bar_start + 4.5)

# Sax Motif: Question, not answer — short, singable, emotional
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62) -> Eb (63) -> F (64) -> rest

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=63, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.75, end=bar_start + 1.125),
    # Leave it hanging — no resolution, just the question
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro.mid")
print("Generated jazz_intro.mid — 4 bars of Dm at 160 BPM")
